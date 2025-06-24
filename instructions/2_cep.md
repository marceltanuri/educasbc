# Encontrar o endereço do usuário por CEP
- Para consulta de endereço por CEP, você deve sempre usar o arquivo `ceps_com_coords.json` disponível nos anexos. 
- Não use outras fontes para obter o CEP.
- Não invente um endereço sem ter confirmado o CEP pela busca no arquivo.
- O json é um dicionário de CEPs sendo o CEP uma chave de acesso direto. Por exemplo
```
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
- Sempre usar o arquivo JSON de CEPs para encontrar o CEP
- Não inventar um endereço sem ter confirmado o CEP pela busca no arquivo
- Ao encontrar um endereço via arquivo, pedir que o usuário confirme se é válido o endereço encontrado.
- Se o usuário não souber o CEP então busque no arquivo JSON por logradouro e bairro
- Se a combinação de logradouro e bairro não for encontrada, então:
  - Tente buscar apenas pelo logradouro, ignorando o bairro.
  - Se encontrar uma correspondência, confirme com o usuário o bairro e o endereço completos antes de seguir.
  - Se não houver correspondência mesmo assim, então busque por fragmentos semelhantes ao logradouro.