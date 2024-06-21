from random import randint


class ProcessQueue:
    def __init__(self, current_queue: list = []) -> None:
        self.__qid = randint(1, 1000)
        self.__current_queue = current_queue
        
    @property
    def qid(self):
        return self.__qid
    
        
    @qid.setter
    def qid(self, qid: int):
        self.__qid = qid
        
    @property
    def current_queue(self):
        return self.__current_queue
    
        
    @current_queue.setter
    def current_queue(self, current_queue: int):
        self.__current_queue = current_queue
    