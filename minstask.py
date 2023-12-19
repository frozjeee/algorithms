class MinStack:

    def __init__(self):
        self.a = []
        self.min = []

    def push(self, val: int) -> None:
        self.a.append(val)
        if self.min:
            val = min(self.min[-1],val)
        self.min.append(val)

    def pop(self) -> None:
        self.a.pop()
        self.min.pop()

    def top(self) -> int:
        return self.a[-1]

    def getMin(self) -> int:
        return self.min[-1]
    

minStack = MinStack()
print(minStack.push(0))
print(minStack.push(-2))
print(minStack.push(-3))
print(minStack.getMin())
print(minStack.pop())
print(minStack.top())
print(minStack.getMin())
print(minStack.pop())
print(minStack.getMin())
 