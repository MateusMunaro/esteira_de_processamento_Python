from write_process import WriteProcess
import json
import os
from menu import Menu
from computation_process import ComputationProcess
from read_process import ReadProcess
from write_process import WriteProcess
from print_process import PrintProcess
from process_queue import ProcessQueue


def create_process(queue: ProcessQueue):
    general_pid = 0
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

        if opt == 1:
            processo = ComputationProcess(general_pid)
            queue.current_queue.append(processo)
        elif opt == 2:
            processo = PrintProcess(general_pid, queue.current_queue)
            processo.execute(queue)
        elif opt == 3:
            processo = ReadProcess(general_pid)
            data = processo.execute(queue)
            

            print("Processos de leitura criados e adicionados à fila com sucesso!")

        elif opt == 4:
            processo = WriteProcess(general_pid)
            processo.execute(queue)
        elif opt == 5:
            break
        else:
            print("Opção inválida.")
            return
        
        
        print("Processo criado e adicionado à fila com sucesso!")

        general_pid += 1


def run_next(queue: ProcessQueue):
    if queue.current_queue:
        queue.current_queue[0].execute()
        queue.current_queue = queue.current_queue[1:]
        print("Processo executado e removido da fila com sucesso!")
    else:
        print("Não há processos na fila para executar.")

def run_specific_process(queue: ProcessQueue):
    pid = int(input("Digite o PID do processo a ser executado: "))
    found = False

    for processo in queue.current_queue:
        if processo.pid == pid:
            found = True
            processo.execute()
            print(f"Processo com PID {pid} executado com sucesso!")
            break

    if not found:
        print("Processo com PID informado não encontrado na fila.")


def save_queue(queue: ProcessQueue, filename: str):
    queue_dict = queue.__dict__()
    with open(filename, 'w') as file:
         json.dump(queue_dict, file)

    print(f'fila de processos salva no arquivo \'{filename}\' com sucesso.')

def load_queue(filename: str) -> ProcessQueue:
    with open(filename, 'r') as file:
        queue_dict = json.load(file)

    return ProcessQueue(**queue_dict)

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
            print("Fila de processos salva com sucesso.")

        elif opt == 5:
            filename = input("Digite o nome do arquivo para carregar a fila de processos: ")
            current_queue = load_queue(filename)
            print("Fila de processos carregada com sucesso.")

        elif opt == 6:
            break
        
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == '__main__':
    main()
