class MinStack:

    def __init__(self):
       self.MinStack = []

    def push(self, val: int) -> None:
        self.MinStack.append(val)

    def pop(self) -> None:
        self.MinStack.pop()
        

    def top(self) -> int:
        return self.MinStack[-1]
        

    def getMin(self) -> int:
        z = 2**31
        for k in self.MinStack:
            if k<z:
                z = k
        return z
        
