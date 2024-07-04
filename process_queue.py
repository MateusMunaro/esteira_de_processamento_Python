from random import randint


class ProcessQueue:
    def __init__(self, qid: int = randint(1, 1000), current_queue: list = []) -> None:
        self.__qid = qid
        self.__current_queue = current_queue
        self.data = 100
        

    def __len__(self):
        return len(self.data)

    def __setitem__(self, index, value):
        if value <= self.max_value:
            self.data[index] = value
        else:
            raise ValueError(f"Value {value} exceeds the maximum allowed value: {self.max_value}")

    def append(self, value):
        self.__setitem__(len(self.data), value)  # Use __setitem__ for validation

    def extend(self, iterable):
        for item in iterable:
            self.append(item)

    def insert(self, index, value):
        if value <= self.max_value:
            self.data.insert(index, value)
        else:
            raise ValueError(f"Value {value} exceeds the maximum allowed value: {self.max_value}")

    def remove(self, value):
        if value in self.data:
            self.data.remove(value)
        else:
            raise ValueError(f"Value {value} not found in the array")

    def __getitem__(self, index):
        return self.data[index]

    def __iter__(self):
        return iter(self.data)

    def __str__(self):
        return str(self.data)

    def clip_existing(self):
        """
        Clips existing elements to the maximum allowed value.
        """
        self.data = [min(x, self.max_value) for x in self.data]



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
    

    def __dict__(self):
        return {
            "qid": self.qid,
            "current_queue": self.current_queue
        }
