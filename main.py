from write_process import WriteProcess
import pickle
import os
from menu import Menu
from computation_process import ComputationProcess
from read_process import ReadProcess
from write_process import WriteProcess
from print_process import PrintProcess
from process_queue import ProcessQueue


def create_process(queue: ProcessQueue):

    while True:
        sub_menu_list = [
            "___Tipos de processo disponíveis:___",
            "1. Processo de Computação",
            "2. Processo de Impressão",
            "3. Processo de Leitura",
            "4. Processo de Escrita",
            "5. Voltar"
        ]
        second_menu = Menu(sub_menu_list)
        opt = second_menu.run()
        processo = None

        if opt == 1:
            expression = input("Digite a expressão a ser executada: ")
            processo = ComputationProcess(expression)
        elif opt == 2:
            document = input("Digite o documento a ser impresso: ")
            processo = PrintProcess(document)
        elif opt == 3:
            file_name = input("Digite o nome do arquivo a ser lido: ")
            processo = ReadProcess(file_name)
        elif opt == 4:
            content = input("Digite o conteúdo a ser escrito: ")
            processo = WriteProcess(content)
        elif opt == 5:
            break
        else:
            print("Opção inválida.")
            return

        queue.current_queue.append(processo)
        print("Processo criado e adicionado à fila com sucesso!")


def run_next(queue: ProcessQueue):
    if queue.current_queue:
        process_menu = queue.current_queue.pop(0)
        process_menu.execute()
        print("Processo executado e removido da fila com sucesso!")
    else:
        print("Não há processos na fila para executar.")

def run_specific_process(queue: ProcessQueue):
    pid = int(input("Digite o PID do processo a ser executado: "))
    found = False

    for i, processo in enumerate(queue.current_queue):
        if processo.pid == pid:
            found = True
            processo.execute()
            queue.current_queue.pop(i)
            print(f"Processo com PID {pid} executado e removido da fila com sucesso!")
            break

    if not found:
        print("Processo com PID informado não encontrado na fila.")

def save_queue(queue: ProcessQueue, filename: str):
    with open(filename, 'wb') as file:
        pickle.dump(queue, file)
    print(f"Fila de processos salva no arquivo '{filename}' com sucesso!")

def load_queue(filename: str) -> ProcessQueue:
    with open(filename, 'rb') as file:
        queue = pickle.load(file)
    print(f"Fila de processos carregada do arquivo '{filename}' com sucesso!")
    return queue

def main() -> None:

    current_queue = ProcessQueue([])


    while True:
        menu_list = [
            "___ Simulador de Execução de Processos ___",
        "Opções:",
        "1 - Criar processos.",
        "2 - Executar próximo.",
        "3 - Executar processo específico.",
        "4 - Salvar a fila de processos.",
        "5 - Carregar do arquivo a fila de processos.",
        "6 - Sair."
        ]

        main_menu = Menu(menu_list)
        opt = main_menu.run()

        if opt == 1:
            create_process(current_queue)

        elif opt == 2:
            run_next(current_queue)
        
        elif opt == 3:
            run_specific_process(current_queue)

        elif opt == 4:
            filename = input("Digite o nome do arquivo para salvar a fila de processos: ")
            save_queue(current_queue, filename)

        elif opt == 5:
            filename = input("Digite o nome do arquivo para carregar a fila de processos: ")
            current_queue = load_queue(filename)

        elif opt == 6:
            break
        
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == '__main__':
    main()
