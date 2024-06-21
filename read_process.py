from process import Process


class ReadProcess(Process):

    def __init__(self, pid: int) -> None:
        super().__init__(pid)

    def execute(self) -> None:
        with open("computation.txt", "r") as f:
            lines = f.readlines()
            print("\nFila de processos no arquivo:")
            for line in lines:
                print(line)


