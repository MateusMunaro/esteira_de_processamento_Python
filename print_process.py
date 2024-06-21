from process import Process


class PrintProcess(Process):
    def __init__(self, pid: int, processlist: list) -> None:
        super().__init__(pid)
        self.__processlist = processlist
        
    def execute(self) -> None:
        for process in self.__processlist:
            print(f"{process.pid} | {process.__name__}")