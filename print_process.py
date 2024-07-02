from process import Process


class PrintProcess(Process):
    def __init__(self, pid: int, processlist: list) -> None:
        super().__init__(pid)
        self.__processlist = processlist

    def __dict__(self):
        return {
            "pid": self.pid,
            "processlist": self.__processlist
            
        }
        
    def execute(self, queue=None) -> None:
        with open("computation.txt", "r") as f:
            lines = f.readlines()
            print("\nFila de processos no arquivo:")
            for line in lines:
                print(line)

        print("\nFila de processos na memoria:")
        for process in self.__processlist:
            print(f"{process.pid} | {process.__class__.__name__}")
