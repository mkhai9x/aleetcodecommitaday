class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.curr_size = 0
        self.max_size = maxSize
        self.increment_list = []

    def push(self, x: int) -> None:
        if self.curr_size != self.max_size:
            self.stack.append(x)
            self.increment_list.append(0)
            self.curr_size += 1

    def pop(self) -> int:
        if self.curr_size == 0:
            return -1
        val = self.stack.pop()
        increment = self.increment_list.pop()
        if self.increment_list:
            self.increment_list[-1] += increment
        self.curr_size -= 1
        return val + increment

    def increment(self, k: int, val: int) -> None:
        valid_index = min(k - 1, self.curr_size - 1)
        if valid_index >= 0:
            self.increment_list[valid_index] += val

if __name__ == '__main__':
    stk = CustomStack(10)
    stk.push(10)
    stk.push(1)
    stk.pop()
    stk.increment(5,100)