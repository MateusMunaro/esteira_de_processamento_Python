from process import Process


class ComputationProcess (Process):
    def __init__(self, pid: int, expression = None, operation = None) -> None:
        super().__init__(pid)
        self.__expression = expression
        self.__operation = operation
        

    @property
    def operation(self):
        return self.__operation

    @operation.setter
    def operation(self, operation):
        self.__operation = operation

    @property
    def expression(self):
        return self.__expression
    
    @expression.setter
    def expression(self, expression):
        self.__expression = expression

    def __dict__(self):
        return {
            "pid": self.pid,
            "expression": self.__expression,
            "type": self.__class__.__name__
        } 

    def execute(self, queue=None) -> None:
        print("Escreva uma expressão que segue os padrões de computação!")
        self.__expression = input("Escreva a expressão: ")
        print("Result: ", eval(self.__expression))
