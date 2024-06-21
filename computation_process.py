from process import Process


class ComputationProcess (Process):
    def __init__(self, pid: int) -> None:
        super().__init__(pid)
        
    def execute(self) -> None:
        n1 = int(input("Type your first number: "))
        n2 = int(input("Type your second number: "))
        print("""
        Select your operation:
        1: +
        2: -
        3: *
        4: /      
        """)
        operation = int(input())
        if operation == 1:
            return f"Result: {n1 + n2}"
        elif operation == 2:
            return f"Result: {n1 - n2}"
        elif operation == 3:
            return f"Result: {n1 * n2}"
        elif operation == 4:
            return f"Result: {n1 / n2}"
        else:
            return f"Operation is not allowed."