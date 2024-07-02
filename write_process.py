import json
from process import Process


class WriteProcess(Process):
    def __init__(self, pid: int) -> None:
        super().__init__(pid)
        
        
    def execute(self, queue) -> None:
        with open("computation.txt", "a") as f:
            for process in queue.current_queue:
                f.writelines(json.dumps(process.__dict__()) + "\n")
