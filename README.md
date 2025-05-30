# Pipeline de Dados: da API ao PostgreSQL

Este projeto realiza um pipeline de ETL desde um endpoint de uma URL de um ERP até o carregamento e armazenamento dos dados num banco de dados PostgreSQL.

## Objetivos do Projeto

1. Criar o pipeline de ETL

2. Armazenar os dados para consultas futuras. 

3. Medir o tempo gasto em todo o Pipeline e o pico de memória durante a execução.

## Etapas

1. **Pré ETL**:

    - Coleta do endpoint da API de vendas do ERP
    - Teste do endpoint via Postman
    - Requisição do tipo POST
    - Autenticação com os headers (content-type, authorization e user-agent)
    - Identificação dos parâmetros e payload (body)
    - Setup de um banco de dados Postegres no Render

2. **Criação de tabela**

    - Conexão com o banco de dados PostgreSQL usando credenciais
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

    - Inserção dos dados no PostgreSQL
    - Criação de condição caso haja conflito

## **Tecnologias e Ferramentas**

- Python 3.11.1
- Bibliotecas:
    - `requests`: para consumir a API
    - `os`: para manipular as variáveis de ambiente
    - `json`: para manipular o payload e extrair os dados
    - `logging`: para printar os checkpoints
    - `datetime`: para manipular datas
    - `sqlalchemy`: para criar o db e armazenar os dados no PostgreSQL
    - `tracemalloc`: para monitorar o pico de memória utilizado durante toda a execução
    - `time`: para medir o tempo de duração da execução de todo o código

- Postman: para testar o endpoint da API
- Render: para hospedar o DB
- PostgreSQL: DB para armazenar os dados
- pgAdmin 4: para acompanhar os dados e executar queries SQL

## Exemplo de Output

<table align="center">
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
      <td style="padding:8px 16px;">2025-01-01 00:00:00</td>
      <td style="padding:8px 16px;">E-Commerce</td>
      <td style="padding:8px 16px;">32,00</td>
      <td style="padding:8px 16px;">1x</td>
      <td style="padding:8px 16px;">30/05/2025 15:37:50.288426</td>
    </tr>
    <tr>
      <td style="padding:8px 16px;">2</td>
      <td style="padding:8px 16px;">2025-02-01 00:00:00</td>
      <td style="padding:8px 16px;">Loja Física</td>
      <td style="padding:8px 16px;">100,00</td>
      <td style="padding:8px 16px;">3x</td>
      <td style="padding:8px 16px;">30/05/2025 15:37:50.288426</td>
    </tr>
    <tr>
      <td style="padding:8px 16px;">3</td>
      <td style="padding:8px 16px;">2025-04-01 00:00:00</td>
      <td style="padding:8px 16px;">E-Commerce</td>
      <td style="padding:8px 16px;">72,00</td>
      <td style="padding:8px 16px;">À Vista</td>
      <td style="padding:8px 16px;">30/05/2025 15:37:50.288426</td>
    </tr>
      </tbody>
</table>



## Estrutura do Projeto

```bash
ETL_API/
├── consultas_SQL/
│   ├── faturamento.sql/ # Qual foi o faturamento total e o numero de vendas da loja no período?
│   ├── parcelamentos.sql/ # Qual foi a forma de parcelamento por categoria no período?
│   ├── parcelas_formatado.sql/ # Formatação de valores da coluna parcelas
│   ├── tkt_medio_mes_categoria.sql/ # Qual foi o ticket médio por mês e categoria?
│   ├── ultimos_registros.sql # Quais foram as 5 últimas vendas?
|   ├── vendas_categoria.sql # Quanto cada categoria vendeu?
|   ├── vendas_mes_categoria.sql # Como foram as vendas por mês e categoria?
├── src/
│   ├── create_db.py/ # Criação do db no PostegreSQL
│   ├── extract.py/ # Extração dos dados
│   ├── load.py/ # Carregamento dos dados
|   ├── transform.py # Transformação dos dados
├── .env.exemplo  # Variáveis de ambiente
├── .gitignore
├── main.py # Roda a ETL
├── README.md 
└── requirements.txt
```

## Contatos

<p>
<!-- LinkedIn -->
    <a href="https://www.linkedin.com/in/irven-xavier/" target="_blank">
      <img
        src="https://img.shields.io/badge/🔗-LinkedIn-0077B5?style=flat-square&logo=linkedin"
        alt="LinkedIn"
        style="margin:4px; height:20px;"
      />
    </a>
<!-- Whatsapp -->
    <a href="https://wa.me/5531991156079/" target="_blank">
      <img
        src="https://img.shields.io/badge/📱-WhatsApp-25D366?style=flat-square&logo=whatsapp"
        alt="WhatsApp"
        style="margin:4px; height:20px;"
      />
    </a>
<!-- Gmail -->
    <a href="mailto:irven.xavier@gmail.com" target="_blank">
      <img
       src="https://img.shields.io/badge/✉️-Email-D14836?style=flat-square&logo=gmail&logoColor=white"
       alt="WhatsApp"
       style="margin:4px; height:20px;"
      />
    </a>
</p>