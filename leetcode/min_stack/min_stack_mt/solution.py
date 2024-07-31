class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.min_stack) == 0 or self.min_stack[-1] >= val:
            self.min_stack.append(val)

    def pop(self) -> None:
        pop_item = None
        if len(self.stack) != 0:
            pop_item = self.stack.pop()
            if pop_item == self.min_stack[-1]:
                self.min_stack.pop()

        return pop_item

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
