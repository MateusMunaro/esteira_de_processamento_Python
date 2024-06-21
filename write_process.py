from process import Process


class WriteProcess(Process):
    def __init__(self, pid: int) -> None:
        super().__init__(pid)
        
        
    def execute(self, queue) -> None:
        with open("computation.txt", "a") as f:
            for item in queue:
                f.write(item)
                f.write("\n")
