class MinStack:
    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.min[-1] if self.min else val)
        self.min.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]

    def __repr__(self):
        return self.stack.__repr__()


if __name__ == "__main__":
    stack = MinStack()
    stack.push(1)
    stack.push(2)
    print(stack)
    print(stack.getMin())
    stack.push(0)
    print(stack)
    print(stack.getMin())

    stack.pop()
    print(stack)
    print(stack.getMin())
    print("--------------")
    stack.pop()
    print(stack)
    print(stack.getMin())
