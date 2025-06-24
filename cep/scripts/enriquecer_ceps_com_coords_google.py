
#!/usr/bin/env python3
import argparse
import json
import os
import sys
from pathlib import Path
from time import sleep
import requests

USER_AGENT = "gpt-matriculas-sbc/1.0"
PAUSA_ENTRE_REQUISICOES = 0.3
MAX_TENTATIVAS = 3
TIMEOUT_S = 10

def consultar_google_maps(endereco: str, api_key: str):
    url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {"address": endereco, "key": api_key}
    try:
        response = requests.get(url, params=params, timeout=TIMEOUT_S)
        if response.status_code == 200:
            data = response.json()
            if data["status"] == "OK" and data["results"]:
                location = data["results"][0]["geometry"]["location"]
                return location["lat"], location["lng"]
    except Exception as e:
        print(f"[ERRO] Erro ao consultar endereço: {endereco} -> {e}")
    return None, None

def enriquecer_ceps(origem_path: Path, cidade: str, estado: str, api_key: str):
    with origem_path.open(encoding="utf-8") as f:
        ceps = json.load(f)

    for cep, dados in ceps.items():
        logradouro = dados.get("logradouro", "")
        bairro = dados.get("bairro", "")
        endereco = f"{logradouro}, {bairro}, {cidade}, {estado}"
        lat, lon = consultar_google_maps(endereco, api_key)
        dados["lat"] = lat
        dados["lon"] = lon
        print(f"[CEP] {cep} → {lat}, {lon}")
        sleep(PAUSA_ENTRE_REQUISICOES)

    saida_path = origem_path.parent / f"{origem_path.stem}_com_coordenadas.json"
    with saida_path.open("w", encoding="utf-8") as f:
        json.dump(ceps, f, ensure_ascii=False, indent=2)
    print(f"Arquivo salvo em: {saida_path}")

def main():
    parser = argparse.ArgumentParser(description="Enriquece um arquivo ceps.json com coordenadas via Google Maps.")
    parser.add_argument("--arquivo", required=True, help="Caminho para o arquivo JSON de entrada.")
    parser.add_argument("--cidade", required=True, help="Nome da cidade.")
    parser.add_argument("--estado", required=True, help="Sigla do estado (ex: SP).")
    args = parser.parse_args()

    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        print("Erro: variável de ambiente GOOGLE_API_KEY não está definida.")
        sys.exit(1)

    origem_path = Path(args.arquivo)
    if not origem_path.exists():
        print(f"Erro: arquivo não encontrado -> {origem_path}")
        sys.exit(1)

    enriquecer_ceps(origem_path, args.cidade, args.estado, api_key)

if __name__ == "__main__":
    main()
