
# 🧠 Agente GPT — Assistente Educacional de São Bernardo do Campo

Este agente GPT foi criado com o [chatgpt-builder](https://github.com/marceltanuri/chatgpt-builder) para atuar como assistente virtual da Secretaria de Educação da Prefeitura de São Bernardo do Campo. Ele orienta responsáveis sobre **a série escolar adequada para uma criança**, com base em **idade, CEP e regras municipais vigentes**.

---

## 📚 Objetivo

Informar com precisão:

- A **etapa** e **série escolar** apropriadas de acordo com a idade da criança em 31 de março do ano letivo solicitado;
- A **obrigatoriedade de matrícula**, quando aplicável;
- As **unidades de ensino mais próximas** da residência informada;
- A **estrutura da rede municipal**, com diferenciação em relação à rede estadual.

---

## 🧩 Estrutura das Instruções

O agente foi configurado com os seguintes arquivos Markdown:

### `1_main.md` — Função e contexto institucional

- O agente representa a Secretaria de Educação de São Bernardo do Campo.
- Atende apenas **Educação Infantil**, **Ensino Fundamental Anos Iniciais (1º ao 5º)** e **EJA**.
- Ensino Fundamental Anos Finais e Ensino Médio são de responsabilidade da **rede estadual**.
- Dados de referência: 220 escolas, 75 mil alunos e 9,8 mil colaboradores (ref. 10/2024).

---

### `2_cep.md` — Busca de endereço por CEP

- Utiliza o arquivo `ceps_com_coords.json` como **única fonte confiável**.
- O JSON é um dicionário com CEPs como chave. Exemplo:
```json
"09600-004": {
  "logradouro": "Avenida Senador Vergueiro",
  "complemento": "- de 2202 a 3798 - lado par",
  "bairro": "Anchieta",
  "codigo_ibge": "8482",
  "bairro_id": "26",
  "lat": -23.6716799948,
  "lon": -46.5406253237
}
```
- O agente **não deve inventar endereços**. Sempre confirmar com o usuário o endereço localizado.

---

### `3_calculo_serie.md` — Cálculo da série escolar

O agente segue **rígidas regras municipais** para associar idade à série:

#### 🗓 Cálculo de idade:
1. Usa a **data de nascimento** e o **ano letivo desejado**;
2. A data de corte é **31 de março** do ano letivo;
3. A idade é expressa em anos e meses;
4. A série escolar é atribuída de acordo com o intervalo de idade.

#### 📘 Tabela de correspondência:
- **0 a 11 meses** ➝ Berçário I (Creche)
- **1 ano** ➝ Berçário II (Creche)
- **2 anos** ➝ Infantil I (Creche)
- **3 anos** ➝ Infantil II (Pré-escola)
- **4 anos** ➝ Infantil III (Pré-escola) — obrigatório
- **5 anos** ➝ Infantil IV (Pré-escola) — obrigatório
- **6 anos** ➝ 1º ano (Ensino Fundamental)
- … até o **5º ano** (10 anos)

#### ⚠️ Exceções:
- Crianças com menos de 2 meses ou mais de 10 anos e 11 meses devem ser encaminhadas para **avaliação individual** na Secretaria de Educação.

---

### `4_enderecos.md` — Unidades de ensino próximas

- O agente utiliza um arquivo de endereços estruturado (`enderecos_com_coords.json`) e as coordenadas de CEP para encontrar as **unidades escolares mais próximas** da residência do aluno.
- A lógica de cálculo utiliza geolocalização e tipo de ensino oferecido (creche, pré-escola, fundamental etc.).

---

## 🔗 Complemento JSON embutido

O agente conta com blocos estruturados em JSON para lookup rápido e integração com código. Inclui:

- Regras de série por idade
- Exemplos canônicos
- Datas de referência

---

## 📦 Requisitos para funcionamento

- `ceps_com_coords.json` — base de CEPs com coordenadas
- `enderecos_com_coords.json` — lista de unidades de ensino
- Instruções estruturadas nos arquivos Markdown listados acima

---

## 🛠️ Builder utilizado

Este agente foi criado com o repositório:

📦 [chatgpt-builder](https://github.com/marceltanuri/chatgpt-builder)

---

## 🧪 Exemplo de pergunta suportada

> **"Meu filho nasceu em 30/06/2022. Qual série ele vai cursar em 2026?"**  
> ➝ O agente responde com idade exata, série recomendada e etapa (ex: Infantil II - Pré-escola).
