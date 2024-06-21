from process import Process


class ReadProcess(Process):

    def __init__(self, pid: int) -> None:
        super().__init__(pid)

    