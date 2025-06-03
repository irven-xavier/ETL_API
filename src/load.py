from src.create_db import engine, tabela_vendas
from sqlalchemy.dialects.postgresql import insert
import logging

logging.basicConfig(
    
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Função para carregar os dados no PostgreSQL
def carregar_dados(dados):

    # Processamento da carga de dados
    try:

        logging.info("Iniciando o carregamento dos dados no PostgreSQL... \n")

        # Insere os valores do dicionário acima na tabela
        stmt = insert(tabela_vendas).values(dados)

        # Em caso de conflito, id existente, os valores não serão adicionandos e nem atualizados
        stmt = stmt.on_conflict_do_nothing(index_elements=['id'])
                                        
        # Começa a conexão com o db                                        
        with engine.begin() as conn:

            # Executa a conexão e insere os dados, se houver mais dados    
            conn.execute(stmt)

        logging.info(f"Carregamento no Postgre concluído: {len(dados)} registros processados. \n")

        return True
    
    # Se houver erro no carregamento
    except Exception as e:

        logging.error(f"Erro no load: {e}")

        return False