from process import Process


class PrintProcess(Process):
    def __init__(self, pid: int) -> None:
        super().__init__(pid)

    def execute(self, queue=None) -> None:
        
        print("\nFila de processos:")

        def check_file_or_create_new():
            try:
                with open("computation.txt", "r") as f:
                    lines = f.readlines()
                    for line in lines:
                        print(line)
            except FileNotFoundError:
                with open("computation.txt", "w") as f:
                    f.write("")

        check_file_or_create_new()

        with open("computation.txt", "r") as f:
            lines = f.readlines()
            print("\nFila de processos no arquivo:")
            for line in lines:
                print(line)

        if queue.current_queue is not None:
            for processo in queue.current_queue:
                print(f"{processo.pid} : {processo.__class__.__name__}")
        else:
            print("Fila de processos vazia.")
