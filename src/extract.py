import json
import os
from dotenv import load_dotenv
import requests

# Carrega as variáveis de ambiente e credenciais
load_dotenv()

api_key = os.getenv("API_TOKEN") # Chave (token) da API
user_agent = os.getenv("USER_AGENT") # Identificador do User agent simulador de navegador
categorias_ids = os.getenv("CATEGORY_IDS", "") # IDs das categorias que quero puxar
url = os.getenv("URL", "") # Url da API em questão

# Transformação dos IDs das categorias em lista
categorias_ids = [x.strip() for x in categorias_ids.split(",") if x.strip()]

page = 1 # Índice inicial da página
page_size = 100 # Tamanho da página (100 registros por vez)

# Cabeçalho da requisição
headers = {

    "x-authorization": api_key,
    "Content-Type": "application/json",
    'user-agent': user_agent
}

# Payload dos Dados (já filtrando data e categorias)
payload=json.dumps(
    {
        "competenceDateFrom": "2025-01-01", # Data Inicial
        "competenceDateTo": "2025-12-31", # Data Final
        "quickFilter": "ALL", # Retira filtros adicionais indesejados
        "categoryIds": categorias_ids, # Categorias de Venda online e Atacado
        "search": "", # Sem pesquisa ativa na barra de pesquisas
        "page": page, # Página Inicial
        "page_size": page_size # Tamanho inicial (100 registros por vez)
    }
)

# Função para extrair os dados da API
def extrair_dados(page, page_size):

  # Dataframe vazio  
  all_data = []

  # Loop para iterar entre as páginas  
  while True:

    # Parâmetros da requisição
    params = {"page": page, "page_size": page_size}

    # Requisição POST na API
    response = requests.post(url, params=params, headers=headers, data=payload)

    # Resposta da API em formato JSON
    dados = response.json()['items']

    if not dados:  # Se não tiver mais dados, para o loop
      print(f"O retorno da API foi o código {response.status_code} \n")
      print(f"Fim da extração. Total de páginas lidas: {page - 1} \n")
      break

    print(f'Dados da página {page} capturados com sucesso \n')
    
    # "Extende" os dados para fora das chaves do retorno JSON
    all_data.extend(dados)

    # Paginação
    page += 1

  return all_data