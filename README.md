# Desafio MBA Engenharia de Software com IA - Full Cycle

O desafio foi desenvolvido seguindo as diretrizes fornecidas utilizando da api google gerada por `https://aistudio.google.com/`.

# Stack
 Seguindo o requirements.txt fornecido no repositório.
 - Python 3.13.5

# Variáveis de ambiente:
- GOOGLE_API_KEY : Chave de API para a LLM 
- GOOGLE_EMBEDDING_MODEL : Modelo do embedding de dados
- DATABASE_URL : String de conexão com o banco de dados
- PG_VECTOR_COLLECTION_NAME : Nome da collection no postgres.
- PDF_PATH : Localização do PDF a ser 'ingerido' pelo PGVector.

# Passos para execução:
1 - Inicialize o PGVector com `docker compose up`
2 - Realize a ingestão dos documentos com `python .\src\ingest.py`
3 - Execute o chat com `python .\src\chat.py`
4 - Faça suas perguntas a respeito do documento e escreva 'sair' para encerrar o chat.

# Testes realizados 

1. Pergunta sobre empresa específica.
```
Faça sua pergunta: Qual o faturamento da SuperTechIABrazil?

Resposta: O faturamento da SuperTechIABrazil é de R$ 10.000.000,00.
```

2. Pergunta geral que abrange várias empresas.
```
Faça sua pergunta: Qual foi a empresa com maior faturamento?

Resposta: A empresa com maior faturamento foi a Aliança Esportes ME, com R$ 4.485.320.049,16.
```

3. Pergunta sobre ano de fundação.
```
Faça sua pergunta: De que ano é a empresa Eon Turismo S.A.?

Resposta: A empresa Eon Turismo S.A. é do ano de 1944.
```

4. Pergunta fora de contexto
```
Faça sua pergunta: Quantos clientes temos de 2024?

Resposta: Não tenho informações necessárias para responder sua pergunta.

```

# Observações
 - Por algum motivo não identificado quando eu pergunto 'Qual o faturamento da empresa SuperTechIABrazil?' ele responde que não tem informações, se eu removo a palavra 'empresa' ele funciona, conforme o teste acima. Como não envolvia tunning do prompt no desafio não alterei o prompt para contemplar esse caso apesar de ser um comportamento 'estranho'.
 - Não houve refatoração / organização do código para que ele seguisse a risca os requisitos de estrutura de pastas do desafio, no máximo extração de metodos para melhor legibilidade.