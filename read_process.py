import json

from process import Process
from computation_process import ComputationProcess

class ReadProcess(Process):

    def __init__(self, pid: int) -> None:
        super().__init__(pid)

    def clean_file(self) -> None:
        with open("computation.txt", "w") as file_object:
            file_object.write("")


    def execute(self, queue) -> None:
        data = []
        with open("computation.txt", "r") as file_object:
            lines = file_object.readlines()
            for line in lines:
                data.append(json.loads(line))
            self.clean_file()    

        for iten in data:
                processo = ComputationProcess(**iten)
                queue.current_queue.append(processo)

        print("Processos de leitura criados e adicionados à fila com sucesso!")

                




