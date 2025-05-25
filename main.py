import time
import tracemalloc
from src.extract import extrair_dados, page, page_size	
from src.transform import tratamento
from src.load import carregar_dados_bulk_upsert

# Função para o pipeline
def main():
    raw = extrair_dados(page, page_size)
    clean = tratamento(raw)
    load = carregar_dados_bulk_upsert(clean)

# Execução do pipeline
if __name__ == "__main__":

    # Inicia o monitoramento de memória
    tracemalloc.start()

    # Início do tempo de execução
    start_time = time.time()

    # Captura o momento inicial
    snapshot_inicio = tracemalloc.take_snapshot()
    
    # Executa a função de extração
    main()

    # Final da Execução
    end_time = time.time()

    # Tempo total de execução
    execution_time = end_time - start_time
    print(f"Tempo de execução: {execution_time:.2f} segundos \n")

    # Captura o momento final
    snapshot_fim = tracemalloc.take_snapshot()

    # Pega o pico de memória durante a execução
    memoria_pico = tracemalloc.get_traced_memory()[1] / (1024 ** 2)  # Em MB

    # Exibe o consumo de memória
    print(f"Pico de memória durante a execução: {memoria_pico:.2f} MB")

    # Para o monitoramento
    tracemalloc.stop()