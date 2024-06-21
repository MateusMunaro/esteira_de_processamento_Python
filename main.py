from write_process import WriteProcess
import os
from menu import Menu
from process import Process
from read_process import ReadProcess
from write_process import WriteProcess
from print_process import PrintProcess


def create_process():

    while True:
        sub_menu_list = [
            "___Tipos de processo disponíveis:___",
            "1. Processo de Computação",
            "2. Processo de Impressão",
            "3. Processo de Leitura",
            "4. Processo de Escrita",
        ]
        second_menu = Menu(sub_menu_list)
        opt = second_menu.run()

        if opt == 1:
            expression = input("Digite a expressão a ser executada: ")
            processo = Process(expression)
        elif opt == 2:
            document = input("Digite o documento a ser impresso: ")
            processo = PrintProcess(document)
        elif opt == 3:
            file_name = input("Digite o nome do arquivo a ser lido: ")
            processo = ReadProcess(file_name)
        elif opt == 4:
            content = input("Digite o conteúdo a ser escrito: ")
            processo = WriteProcess(content)
        else:
            print("Opção inválida.")
            return

        fila_de_processos.append(processo)
        print("Processo criado e adicionado à fila com sucesso!")

fila_de_processos = []

def main() -> None:

    while True:
        menu_list = [
            "___ Simulador de Execução de Processos ___",
        "Opções:",
        "1 - Criar processos.",
        "2 - Executar próximo.",
        "3 - Executar processo específico.",
        "4 - Salvar a fila de processos.",
        "5 - Carregar do arquivo a fila de processos.",
        ]

        main_menu = Menu(menu_list)
        opt = main_menu.run()

        if opt == 1:
            create_process()

        elif opt == 2:
            pass
        
        elif opt == 3:
            print("Programa encerrado.")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == '__main__':
    main()