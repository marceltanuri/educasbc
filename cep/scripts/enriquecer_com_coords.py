#!/usr/bin/env python3
"""
enriquecer_com_coords.py
Enriquece arquivos JSON (ceps.json ou enderecos.json) com latitude/longitude
usando a API https://www.cepaberto.com  (é preciso informar --token).

Exemplos:
  python enriquecer_com_coords.py --pasta ./dados --tipo ceps --token SEU_TOKEN
  python enriquecer_com_coords.py --pasta ./dados --tipo enderecos --token SEU_TOKEN
"""
import argparse
import json
import sys
from pathlib import Path
from time import sleep
import requests

USER_AGENT = "gpt-matriculas-sbc/1.0"
PAUSA_ENTRE_REQUISICOES = 0.3       # segundos entre requisições (evita burst)
MAX_TENTATIVAS = 3                  # tentativas por CEP quando não retorna coordenadas
TIMEOUT_S = 10                      # timeout de rede

# ──────────────────────────────────────────────────────────────────────────────
# Helpers
# ──────────────────────────────────────────────────────────────────────────────
def consultar_cep_aberto(cep: str, token: str) -> tuple[float | None, float | None]:
    """
    Consulta o CEP na API do CEP Aberto.
    Retorna (lat, lon) como floats ou (None, None) se não encontrado.
    Executa até MAX_TENTATIVAS retentativas se latitude/longitude vier vazia.
    """
    cep_numerico = cep.replace("-", "")
    url = f"https://www.cepaberto.com/api/v3/cep?cep={cep_numerico}"
    headers = {"Authorization": f"Token token={token}", "User-Agent": USER_AGENT}

    for tentativa in range(1, MAX_TENTATIVAS + 1):
        try:
            resp = requests.get(url, headers=headers, timeout=TIMEOUT_S)
            if resp.status_code == 200:
                dados = resp.json()
                lat = float(dados["latitude"]) if dados.get("latitude") else None
                lon = float(dados["longitude"]) if dados.get("longitude") else None
                if lat and lon:
                    return lat, lon
            else:
                print(f"[WARN] CEP {cep}: HTTP {resp.status_code}")
        except requests.RequestException as e:
            print(f"[ERRO] CEP {cep}: {e}")

        if tentativa < MAX_TENTATIVAS:
            sleep(1)  # breve espera antes da próxima tentativa
    return None, None


# ──────────────────────────────────────────────────────────────────────────────
# Processadores
# ──────────────────────────────────────────────────────────────────────────────
def enriquecer_ceps(origem: Path, token: str):
    entrada = origem / "ceps.json"
    saida = origem / "ceps_com_coords.json"

    with entrada.open(encoding="utf-8") as f:
        ceps = json.load(f)

    for cep, dados in ceps.items():
        lat, lon = consultar_cep_aberto(cep, token)
        dados["lat"] = lat
        dados["lon"] = lon
        print(f"[CEP] {cep} → {lat}, {lon}")
        sleep(PAUSA_ENTRE_REQUISICOES)

    with saida.open("w", encoding="utf-8") as f:
        json.dump(ceps, f, ensure_ascii=False, indent=2)


def enriquecer_unidades(origem: Path, token: str):
    entrada = origem / "enderecos.json"
    saida = origem / "enderecos_com_coords.json"

    with entrada.open(encoding="utf-8") as f:
        unidades = json.load(f)

    for unidade in unidades:
        cep = unidade.get("CEP", "").strip()
        if not cep:
            print(f"[WARN] Unidade sem CEP: {unidade.get('NOME_DA_UNIDADE_DE_ENSINO')}")
            lat = lon = None
        else:
            lat, lon = consultar_cep_aberto(cep, token)
        unidade["lat"] = lat
        unidade["lon"] = lon
        print(f"[UNID] {unidade['NOME_DA_UNIDADE_DE_ENSINO']} ({cep}) → {lat}, {lon}")
        sleep(PAUSA_ENTRE_REQUISICOES)

    with saida.open("w", encoding="utf-8") as f:
        json.dump(unidades, f, ensure_ascii=False, indent=2)


# ──────────────────────────────────────────────────────────────────────────────
# CLI
# ──────────────────────────────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(
        description="Enriquece ceps.json ou enderecos.json com latitude/longitude via CEP Aberto."
    )
    parser.add_argument("--pasta", required=True, help="Diretório contendo os JSONs")
    parser.add_argument(
        "--tipo",
        required=True,
        choices=["ceps", "enderecos"],
        help='Escolha "ceps" para processar ceps.json ou "enderecos" para enderecos.json',
    )
    parser.add_argument("--token", required=True, help="Token da API do CEP Aberto")

    args = parser.parse_args()
    pasta = Path(args.pasta)

    if not pasta.is_dir():
        print(f"Pasta inválida: {pasta}")
        sys.exit(1)

    if args.tipo == "ceps":
        enriquecer_ceps(pasta, args.token)
    else:  # enderecos
        enriquecer_unidades(pasta, args.token)


if __name__ == "__main__":
    main()
