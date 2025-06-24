#!/usr/bin/env python3
"""
Script: enriquecer_enderecos_com_coords_google.py
Enriquece um arquivo enderecos.json com latitude/longitude consultando a API do Google Maps.
A chave da API deve estar na variável de ambiente GOOGLE_API_KEY.

Uso:
  python enriquecer_enderecos_com_coords_google.py --arquivo ./dados/enderecos.json --cidade "São Bernardo do Campo" --estado SP
"""

import argparse
import json
import os
import sys
from pathlib import Path
from time import sleep
import requests

USER_AGENT = "educasbc-geocode/1.0"
PAUSA_ENTRE_REQUISICOES = 0.3
MAX_TENTATIVAS = 3
TIMEOUT_S = 10

def montar_endereco(unidade: dict, cidade: str, estado: str) -> str:
    partes = [unidade.get("ENDEREÇO", ""), unidade.get("BAIRRO", ""), cidade, estado]
    return ", ".join([parte for parte in partes if parte])

def consultar_google(endereco: str, api_key: str) -> tuple[float | None, float | None]:
    url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {"address": endereco, "key": api_key}
    for tentativa in range(1, MAX_TENTATIVAS + 1):
        try:
            resp = requests.get(url, params=params, timeout=TIMEOUT_S)
            if resp.status_code == 200:
                dados = resp.json()
                if dados["status"] == "OK" and dados["results"]:
                    local = dados["results"][0]["geometry"]["location"]
                    return local["lat"], local["lng"]
                else:
                    print(f"[WARN] Endereço '{endereco}' não encontrado.")
            else:
                print(f"[WARN] Erro HTTP {resp.status_code} para '{endereco}'")
        except requests.RequestException as e:
            print(f"[ERRO] '{endereco}': {e}")
        if tentativa < MAX_TENTATIVAS:
            sleep(1)
    return None, None

def enriquecer_enderecos(caminho_arquivo: Path, cidade: str, estado: str, api_key: str):
    with caminho_arquivo.open(encoding="utf-8") as f:
        unidades = json.load(f)

    for unidade in unidades:
        endereco = montar_endereco(unidade, cidade, estado)
        lat, lon = consultar_google(endereco, api_key)
        unidade["lat"] = lat
        unidade["lon"] = lon
        print(f"[OK] {unidade.get('NOME_DA_UNIDADE_DE_ENSINO', 'Desconhecida')} → {lat}, {lon}")
        sleep(PAUSA_ENTRE_REQUISICOES)

    arquivo_saida = caminho_arquivo.with_name(caminho_arquivo.stem + "_com_coordenadas.json")
    with arquivo_saida.open("w", encoding="utf-8") as f:
        json.dump(unidades, f, ensure_ascii=False, indent=2)

def main():
    parser = argparse.ArgumentParser(description="Enriquece enderecos.json com coordenadas via Google Maps.")
    parser.add_argument("--arquivo", required=True, help="Caminho para o arquivo enderecos.json")
    parser.add_argument("--cidade", required=True, help="Nome da cidade")
    parser.add_argument("--estado", required=True, help="Sigla do estado (ex: SP)")
    args = parser.parse_args()

    caminho_arquivo = Path(args.arquivo)
    if not caminho_arquivo.is_file():
        print(f"Arquivo inválido: {caminho_arquivo}")
        sys.exit(1)

    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        print("Erro: a variável de ambiente GOOGLE_API_KEY não está definida.")
        sys.exit(1)

    enriquecer_enderecos(caminho_arquivo, args.cidade, args.estado, api_key)

if __name__ == "__main__":
    main()
