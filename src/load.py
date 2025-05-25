from src.create_db import engine, meu_db
from sqlalchemy.dialects.postgresql import insert

def carregar_dados_bulk_upsert(dados):
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
    stmt = stmt.on_conflict_do_update(
        index_elements=['id'],
        set_={
            "data": stmt.excluded.data,
            "categoria": stmt.excluded.categoria,
            "valor": stmt.excluded.valor,
            "parcelas": stmt.excluded.parcelas,
            "data_extracao": stmt.excluded.data_extracao,
        }
    )
    with engine.begin() as conn:
        conn.execute(stmt)
    print("Bulk upsert realizado no PostgreSQL.\n")