from datetime import datetime
from src.create_db import meu_db

# Função para tratar os dados do retorno da API
def tratamento(lista_items):
    
    return [
        
        meu_db(
            id = item['id'], # ID da transação
            data = item['competenceDate'], # Data de competência da transação
            categoria = item['categoryDescriptions'], # Categoria da transação
            valor = item['value'], # Valor da categoria
            parcelas = item['paymentCondition'], # Nº de parcelas da transação
            data_extracao = datetime.now().isoformat() # Data da captura dos dados
        )

        # List comprehension para iterar em cada retorno de página
        for item in lista_items

    ]