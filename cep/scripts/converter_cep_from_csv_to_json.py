import csv
import json
import argparse

# ----------------------------------------
# 🔧 PARSE DOS PARÂMETROS
# ----------------------------------------

parser = argparse.ArgumentParser(
    description="Converte um arquivo CSV de CEPs para um JSON estruturado por CEP como chave."
)

parser.add_argument(
    "--entrada", required=True,
    help="Caminho para o arquivo CSV de entrada (ex: ceps_sbc.csv)"
)

parser.add_argument(
    "--saida", required=True,
    help="Caminho do arquivo JSON de saída (ex: ceps_sbc_por_cep.json)"
)

args = parser.parse_args()

ARQUIVO_CSV = args.entrada
ARQUIVO_JSON = args.saida

# ----------------------------------------
# 🔄 CONVERSÃO DE CSV PARA JSON INDEXADO POR CEP
# ----------------------------------------

dados_por_cep = {}

with open(ARQUIVO_CSV, newline='', encoding='utf-8') as csvfile:
    leitor = csv.reader(csvfile)
    for linha in leitor:
        if len(linha) != 6:
            continue  # ignora linhas incompletas

        cep_raw, logradouro, complemento, bairro, codigo_ibge, bairro_id = linha
        cep_formatado = f"{cep_raw[:5]}-{cep_raw[5:]}"  # Ex: 09600004 → 09600-004

        dados_por_cep[cep_formatado] = {
            "logradouro": logradouro,
            "complemento": complemento,
            "bairro": bairro
        }

# Ordena por CEP para facilitar buscas futuras
dados_ordenados = dict(sorted(dados_por_cep.items()))

with open(ARQUIVO_JSON, "w", encoding="utf-8") as jsonfile:
    json.dump(dados_ordenados, jsonfile, ensure_ascii=False, indent=2)

print(f"✅ Arquivo JSON gerado com {len(dados_ordenados)} CEPs em '{ARQUIVO_JSON}'.")
