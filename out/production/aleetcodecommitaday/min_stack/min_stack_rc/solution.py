class MinStack:

    def __init__(self):
        self.stack = []
        self.min_val = None
        self.length = 0

    def push(self, val: int) -> None:
        if self.min_val is None:
            self.min_val = val
        else:
            self.min_val = min(self.getMin(), val)
        print(self.min_val)
        self.stack.append([val, self.min_val])
        self.length += 1

    def pop(self) -> None:
        self.stack.pop()
        self.length -= 1
        if self.length == 0:
            self.min_val = None
        else:
            self.min_val = self.getMin()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
