from process import Process


class ComputationProcess (Process):
    def __init__(self, pid: int, n1: int = 0, n2: int = 0, operation = None) -> None:
        super().__init__(pid)
        self.__n1 = n1
        self.__n2 = n2
        self.__operation = operation
        

    @property
    def n1(self):
        return self.__n1

    @property
    def n2(self):
        return self.__n2

    @property
    def operation(self):
        return self.__operation
    
    @n1.setter
    def n1(self, n1):
        self.__n1 = n1

    @n2.setter
    def n2(self, n2):
        self.__n2 = n2

    @operation.setter
    def operation(self, operation):
        self.__operation = operation

    def __dict__(self):
        return {
            "pid": self.pid,
            "n1": self.__n1,
            "n2": self.__n2,
            "operation": self.__operation
        } 

    def execute(self, queue=None) -> None:
        self.__n1 = int(input("Type your first number: "))
        self.__n2 = int(input("Type your second number: "))
        print("""
        Select your operation:
        1: +
        2: -
        3: *
        4: /      
        """)
        self.__operation = int(input())
        if self.__operation == 1:
            print(f"Result: {self.__n1 + self.__n2}")
        elif self.__operation == 2:
            print(f"Result: {self.__n1 - self.__n2}")
        elif self.__operation == 3:
            print(f"Result: {self.__n1 * self.__n2}")
        elif self.__operation == 4:
            print(f"Result: {self.__n1 / self.__n2}")
        else:
            print(f"Operation is not allowed.")