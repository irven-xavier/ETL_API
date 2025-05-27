# Pipeline de Dados: da API ao Postgres

## Objetivo

Criar um pipeline a partir de um endpoint de uma API utilizando Python para fazer a extração, transformação e carregamento até uma tabela criada, também com Python, no Postgres SQL. 

## Etapas

1. **Pré ETL**:

    - Endpoint da API de vendas de um ERP
    - Teste do endpoint via Postman
    - Requisição do tipo POST
    - Autenticação com os headers (content-type, authorization e user-agent)
    - Identificação dos parâmetros e payload(body)
    - Setup de um banco de dados Postegres no Render

2. **Criação de tabela**

    - Conexão com o banco de dados Postgre usando credenciais
    - Início da sessão e criação do modelo no Postegre

3. **Extração**:

    - Manipulação dos requisitos do endpoint
    - Definição dos parâmetros e variáveis 
    - Criação de loop While para paginação

4. **Transformação**:

    - Seleção de 5 chaves de 24 possíveis do arquivo json
    - Organizar seleção na ordem desejada
    - Criação de uma coluna com a data de extração dos dados

5. **Carregamento**:

    - Inserção dos dados no Postgre
    - Criação de condição caso haja conflito

## **Tecnologias**

- Python 3.11.1
- Bibliotecas:
    - `requests`: para consumir a API
    - `os`: para 
    - `sqlalchemy`:
    - `sqlalchemy`:
    - `sqlalchemy`:
    - `sqlalchemy`:
    - `sqlalchemy`:
