from src.create_db import engine, meu_db
from sqlalchemy.dialects.postgresql import insert
import logging

logging.basicConfig(
    
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def carregar_dados(dados):

    try:

        data_dicts = [

            {
                "id": d.id,
                "data": d.data,
                "categoria": d.categoria,
                "valor": d.valor,
                "parcelas": d.parcelas,
                "data_extracao": d.data_extracao,
            }

            for d in dados

        ]
        
        stmt = insert(meu_db).values(data_dicts)

        stmt = stmt.on_conflict_do_nothing(index_elements=['id'])
                                        
        with engine.begin() as conn:

            conn.execute(stmt)

        logging.info(f"Carregamento no Postgre concluído: {len(data_dicts)} registros processados. \n")

        return True
    
    except Exception as e:

        logging.error(f"Erro no load: {e}")

        return False