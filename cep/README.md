# 📍 Atualização da Base de CEPs e Unidades de Ensino

Este repositório contém scripts e procedimentos para manter atualizada a base de **CEPs** e **unidades de ensino** do município, com enriquecimento geográfico (latitude e longitude), usada em um assistente GPT customizado.

---

## 🗂 Estrutura de Pastas

```
cep/
├── data/                          # CSVs originais da CEP Aberto
├── ceps_filtrados_XXXXX.csv       # Resultado do filtro por cidade
├── ceps.json                      # JSON convertido do CSV
├── ceps_com_coords.json           # CEPs com latitude/longitude
├── enderecos.json                 # Unidades de ensino (extração manual)
├── enderecos_com_coords.json      # Endereços com latitude/longitude
└── scripts/
    ├── filtrar_por_cidade.py
    ├── converter_cep_from_csv_to_json.py
    └── enriquecer_com_coords.py
```

---

## 🔁 Procedimento de Atualização

### 1. Baixar os arquivos CSV do site da [CEP Aberto](https://www.cepaberto.com/downloads/new)
- Salve os arquivos na pasta `cep/data`

### 2. Filtrar somente os CEPs da cidade desejada

```bash
python cep/scripts/filtrar_por_cidade.py \
  --origem cep/data \
  --cidade-id 7107 \
  --estado-id 26
```

> 📌 Obs: Os IDs de cidade e estado estão disponíveis no site da CEP Aberto.

---

### 3. Converter CSV para JSON indexado por CEP

```bash
python cep/scripts/converter_cep_from_csv_to_json.py \
  --entrada cep/data/ceps_filtrados_7107.csv \
  --saida cep/ceps.json
```

---

### 4. Enriquecer os dados com coordenadas geográficas

#### 4.1 Enriquecer os CEPs:

```bash
python cep/scripts/enriquecer_com_coords.py \
  --pasta cep \
  --tipo ceps \
  --token SEU_TOKEN_DA_CEP_ABERTO
```

#### 4.2 Enriquecer os endereços das unidades:

```bash
python cep/scripts/enriquecer_com_coords.py \
  --pasta cep \
  --tipo enderecos \
  --token SEU_TOKEN_DA_CEP_ABERTO
```

> 💡 O arquivo `enderecos.json` deve ser atualizado manualmente a partir da versão mais recente do PDF fornecido pela Secretaria da Educação.

---

### 5. Enviar os arquivos `ceps_com_coords.json` e `enderecos_com_coords.json` para o GPT Customizado

No painel de criação do GPT, inclua esses arquivos como uploads, garantindo que o agente possa cruzar CEPs e calcular proximidade com precisão.

---

## 💡 Dicas

- Utilize uma taxa de requisição segura (ex: 1s) para evitar bloqueio na API da CEP Aberto.
- O script `enriquecer_com_coords.py` realiza até 3 tentativas se a coordenada não for encontrada de primeira.

---

## 📌 Requisitos

- Python 3.8+
- Bibliotecas: `requests`

Instale com:

```bash
pip install -r requirements.txt
```

`requirements.txt`:

```
requests>=2.28
```

---

## ✍️ Autoria

Este repositório foi organizado por Marcel Tanuri para manter atualizada e georreferenciada a base de dados utilizada por um assistente GPT especializado em Educação Municipal.
