from random import randint
from write_process import WriteProcess
import json
from menu import Menu
from computation_process import ComputationProcess
from read_process import ReadProcess
from write_process import WriteProcess
from print_process import PrintProcess
from process_queue import ProcessQueue


class MainExecution:

    def create_process(self, queue: ProcessQueue):
        general_pid = randint(1, 10000)
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
                processo.execute(queue)
                queue.current_queue.append(processo)
            elif opt == 2:
                processo = PrintProcess(general_pid)
                processo.execute(queue)
                queue.current_queue.append(processo)
            elif opt == 3:
                processo = ReadProcess(general_pid)
                data = processo.execute(queue)
                queue.current_queue.append(processo)
                

                print("Processos de leitura criados e adicionados à fila com sucesso!")

            elif opt == 4:
                processo = WriteProcess(general_pid)
                processo.execute(queue)
                queue.current_queue.append(processo)
            elif opt == 5:
                break
            else:
                print("Opção inválida.")
                return
            
            
            print("Processo criado e adicionado à fila com sucesso!")

            general_pid += randint(1, 3)


    def run_next(self, queue: ProcessQueue):
        if queue.current_queue:
            queue.current_queue[0].execute(queue)
            queue.current_queue.pop(0)
            print("Processo executado e removido da fila com sucesso!")
        else:
            print("Não há processos na fila para executar.")

    def run_specific_process(self, queue: ProcessQueue):
        pid = int(input("Digite o PID do processo a ser executado: "))

        for processo in queue.current_queue:
            if processo.pid == pid:
                print("Processo com PID informado encontrado na fila.")
                processo.execute(queue)
                break   
        # remove the process from the queue
        queue.current_queue = [p for p in queue.current_queue if p.pid != pid]

    def save_queue(self, queue: ProcessQueue, filename: str):
        with open(filename, 'w') as file:
            for p in queue.current_queue:
                file.write(json.dumps(p.__dict__()) + '\n')

        print(f'fila de processos salva no arquivo \'{filename}\' com sucesso.')


    def load_queue(self, filename: str, queue: ProcessQueue):
        with open(filename, 'r') as file:
            lines = file.readlines()
            queue_dict = {}
            for line in lines:
                data = json.loads(line)
                print(data)
                data_with_no_type = {k: v for k, v in data.items() if k != 'type'}
                if data["type"] == "ComputationProcess":
                    queue.current_queue.append(ComputationProcess(**data_with_no_type))
                elif data["type"] == "PrintProcess":
                    queue.current_queue.append(PrintProcess(**data_with_no_type))
                elif data["type"] == "ReadProcess":
                    queue.current_queue.append(ReadProcess(**data_with_no_type))
                elif data["type"] == "WriteProcess":
                    queue.current_queue.append(WriteProcess(**data_with_no_type))
        

    def main(self) -> None:

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
                self.create_process(current_queue)

            elif opt == 2:
                self.run_next(current_queue)
            
            elif opt == 3:
                self.run_specific_process(current_queue)

            elif opt == 4:
                filename = input("Digite o nome do arquivo para salvar a fila de processos: ")
                self.save_queue(current_queue, filename)
                print("Fila de processos salva com sucesso.")

            elif opt == 5:
                filename = input("Digite o nome do arquivo para carregar a fila de processos: ")
                self.load_queue(filename, current_queue)
                print("Fila de processos carregada com sucesso.")

            elif opt == 6:
                break
            
            else:
                print("Opção inválida. Tente novamente.")

if __name__ == '__main__':
    exe = MainExecution()
    exe.main()
