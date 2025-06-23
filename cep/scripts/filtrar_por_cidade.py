import csv
import os
import argparse

# ----------------------------------------
# 🔧 PARSE DOS PARÂMETROS
# ----------------------------------------

parser = argparse.ArgumentParser(
    description="Filtra arquivos CSV contendo CEPs com base em cidadeId e estadoId."
)

parser.add_argument(
    "--origem", required=True,
    help="Pasta de origem contendo arquivos CSV."
)

parser.add_argument(
    "--cidade-id", required=True,
    help="ID da cidade (obtido do site da CEP Aberto)."
)

parser.add_argument(
    "--estado-id", required=True,
    help="ID do estado (obtido do site da CEP Aberto)."
)

args = parser.parse_args()

PASTA_ORIGEM = args.origem
CIDADE_ID_ALVO = args.cidade_id
ESTADO_ID_ALVO = args.estado_id

ARQUIVO_SAIDA = os.path.join(PASTA_ORIGEM, f"ceps_filtrados_{CIDADE_ID_ALVO}.csv")

# ----------------------------------------
# 📝 OBSERVAÇÃO:
# Baixe os códigos de cidade e estado em:
# https://www.cepaberto.com/downloads/new
# ----------------------------------------

linhas_filtradas = []

for nome_arquivo in os.listdir(PASTA_ORIGEM):
    if not nome_arquivo.endswith(".csv"):
        continue

    caminho_arquivo = os.path.join(PASTA_ORIGEM, nome_arquivo)
    with open(caminho_arquivo, newline='', encoding='utf-8') as csvfile:
        leitor = csv.reader(csvfile)
        for linha in leitor:
            if len(linha) != 6:
                continue

            cep, logradouro, complemento, bairro, cidade_id, estado_id = linha
            if cidade_id == CIDADE_ID_ALVO and estado_id == ESTADO_ID_ALVO:
                linhas_filtradas.append(linha)

# Salva o CSV final
with open(ARQUIVO_SAIDA, "w", newline='', encoding='utf-8') as saida_csv:
    escritor = csv.writer(saida_csv)
    escritor.writerows(linhas_filtradas)

print(f"✅ Total de linhas filtradas: {len(linhas_filtradas)}")
print(f"📁 Arquivo gerado: {ARQUIVO_SAIDA}")
