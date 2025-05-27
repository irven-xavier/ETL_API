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
    - `os`: para manipular as variáveis de ambiente
    - `json`: para manipular o payload e extrair os dados
    - `logging`: para printar os checkpoints
    - `datetime`: para manipular datas
    - `sqlalchemy`: para criar o db e armazenar os dados no Postgre
    - `tracemalloc`: para monitorar o pico de memória utilizado durante toda a execução
    - `time`: para medir o tempo de duração da execução de todo o código

## Exemplo de Output

<table align="left">
  <thead>
    <tr>
      <th align="left" style="padding:8px 16px;background:#f0f0f0;">id</th>
      <th align="left" style="padding:8px 16px;background:#f0f0f0;">data</th>
      <th align="left" style="padding:8px 16px;background:#f0f0f0;">categoria</th>
      <th align="left" style="padding:8px 16px;background:#f0f0f0;">valor</th>
      <th align="left" style="padding:8px 16px;background:#f0f0f0;">parcelas</th>
      <th align="left" style="padding:8px 16px;background:#f0f0f0;">data_extracao</th>
    </tr>
  </thead>
<tbody>
    <tr>
      <td style="padding:8px 16px;">1</td>
      <td style="padding:8px 16px;">2025-01-01 14:00:00</td>
      <td style="padding:8px 16px;">E-Commerce</td>
      <td style="padding:8px 16px;">32,00</td>
      <td style="padding:8px 16px;">1x</td>
      <td style="padding:8px 16px;">30/05/2021 16:00:00</td>
    </tr>
    <tr>
      <td style="padding:8px 16px;">2</td>
      <td style="padding:8px 16px;">2025-02-01 16:00:00</td>
      <td style="padding:8px 16px;">Loja Física</td>
      <td style="padding:8px 16px;">100,00</td>
      <td style="padding:8px 16px;">3x</td>
      <td style="padding:8px 16px;">30/05/2021 16:00:00</td>
    </tr>
    <tr>
      <td style="padding:8px 16px;">3</td>
      <td style="padding:8px 16px;">2025-04-01 18:00:00</td>
      <td style="padding:8px 16px;">E-Commerce</td>
      <td style="padding:8px 16px;">72,00</td>
      <td style="padding:8px 16px;">À Vista</td>
      <td style="padding:8px 16px;">30/05/2021 16:00:00</td>
    </tr>
      </tbody>
</table>