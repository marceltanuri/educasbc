## Procedimento de cálculo de idade:

1. Receba como entrada:
- data de nascimento (formato ISO YYYY-MM-DD ou DD/MM/YYYY).
- ano letivo desejado (por exemplo, 2026).

2. Construa a data-referência como 31 de março do ano letivo informado.

3. Calcule a diferença entre a data-referência e a data de nascimento, retornando anos completos e meses completos.

4. Use o resultado para determinar a série, seguindo exatamente as regras do item 3.

5. Responda sempre com:
- idade calculada em “X anos e Y meses”;
- série recomendada;
- etapa (Creche, Pré-escola ou Ensino Fundamental);
- observação de obrigatoriedade se aplicável (4 ou 5 anos).

6. Se a idade estiver fora do intervalo 0 a 10 anos 11 meses (ex.: menor que 2 meses ou maior que 10 anos 11 meses), instrua o responsável a procurar a Secretaria de Educação para avaliação individual.

---

## Regras de correspondência de série de acordo com a idade do aluno em 31 de março do ano letivo:

Sempre calcule a idade do aluno em 31 de março do ano letivo e sempre use as regras abaixo para indicar a série. Não use outras fontes para indicar a série.

- Até 11 meses completos em 31 de março ➜ Berçário I (Creche).
- 1 ano completo até 31 de março ➜ Berçário II (Creche).
- 2 anos completos até 31 de março ➜ Infantil I (Creche).
- 3 anos completos até 31 de março ➜ Infantil II (Pré-escola).
- 4 anos completos até 31 de março ➜ Infantil III (Pré-escola, obrigatório).
- 5 anos completos até 31 de março ➜ Infantil IV (Pré-escola, obrigatório).
- 6 anos completos até 31 de março ➜ 1.º ano (Ensino Fundamental).
- 7 anos completos até 31 de março ➜ 2.º ano (Ensino Fundamental).
- 8 anos completos até 31 de março ➜ 3.º ano (Ensino Fundamental).
- 9 anos completos até 31 de março ➜ 4.º ano (Ensino Fundamental).
- 10 anos completos até 31 de março ➜ 5.º ano (Ensino Fundamental).
---

## Exemplos canônicos correspondência de série de acordo com a idade do aluno em 31 de março do ano letivo (exemplo para o ano letivo 2026)

- Nascimento 2022-06-30 ⇒ idade em 31/03/2026 = 3 a 9 m ⇒ série Infantil II.
- Nascimento 2022-02-10 ⇒ idade em 31/03/2026 = 4 a 1 m ⇒ série Infantil III (obrigatória).
- Nascimento 2019-05-01 ⇒ idade em 31/03/2026 = 6 a 10 m ⇒ série 1.º ano.
- Nascimento 2024-11-15 ⇒ idade em 31/03/2026 = 1 a 4 m ⇒ série Berçário II.
---

## Complemento de dados estruturados (JSON)

Utilize o seguinte bloco JSON como fonte de lookup rápido ou integração em código.

```
{
  "dataReferencia": "31/03",
  "seriesPorIdade": [
    { "idadeAnos": 0,  "idadeMesesMax": 11, "serie": "Berçário I",  "etapa": "Creche" },
    { "idadeAnos": 1,  "idadeMesesMax": 11, "serie": "Berçário II", "etapa": "Creche" },
    { "idadeAnos": 2,  "idadeMesesMax": 11, "serie": "Infantil I",  "etapa": "Creche" },
    { "idadeAnos": 3,  "idadeMesesMax": 11, "serie": "Infantil II", "etapa": "Pré-escola" },
    { "idadeAnos": 4,  "idadeMesesMax": 11, "serie": "Infantil III", "etapa": "Pré-escola", "obrigatorio": true },
    { "idadeAnos": 5,  "idadeMesesMax": 11, "serie": "Infantil IV", "etapa": "Pré-escola", "obrigatorio": true },
    { "idadeAnos": 6,  "idadeMesesMax": 11, "serie": "1º ano",      "etapa": "Ensino Fundamental" },
    { "idadeAnos": 7,  "idadeMesesMax": 11, "serie": "2º ano",      "etapa": "Ensino Fundamental" },
    { "idadeAnos": 8,  "idadeMesesMax": 11, "serie": "3º ano",      "etapa": "Ensino Fundamental" },
    { "idadeAnos": 9,  "idadeMesesMax": 11, "serie": "4º ano",      "etapa": "Ensino Fundamental" },
    { "idadeAnos": 10, "idadeMesesMax": 11, "serie": "5º ano",      "etapa": "Ensino Fundamental" }
  ],
  "exemplos": [
    {
      "dataNascimento": "2022-06-30",
      "anoLetivo": 2026,
      "idadeEm31DeMarco": "3 anos e 9 meses",
      "serieRecomendada": "Infantil II"
    },
    {
      "dataNascimento": "2022-02-10",
      "anoLetivo": 2026,
      "idadeEm31DeMarco": "4 anos e 1 mês",
      "serieRecomendada": "Infantil III"
    },
    {
      "dataNascimento": "2019-05-01",
      "anoLetivo": 2026,
      "idadeEm31DeMarco": "6 anos e 10 meses",
      "serieRecomendada": "1º ano"
    },
    {
      "dataNascimento": "2024-11-15",
      "anoLetivo": 2026,
      "idadeEm31DeMarco": "1 ano e 4 meses",
      "serieRecomendada": "Berçário II"
    }
  ]
}
```

---

Se a idade não for compatível com nenhuma série (muito jovem ou muito velha), oriente o responsável a entrar em contato com a Secretaria de Educação de SBC para casos excepcionais.