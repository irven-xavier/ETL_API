from datetime import datetime
from src.create_db import tabela_vendas

# Função para tratar os dados do retorno da API
def tratamento(lista_items):
    
    return [
        # Cria um dicionário para cada item com os campos necessários
        {

            "id": item['id'],
            "data": item['competenceDate'],
            "categoria": item['categoryDescriptions'],
            "valor": item['value'],
            "parcelas": item['paymentCondition'],
            "data_extracao": datetime.now().isoformat()

        }
        
        for item in lista_items
    ]