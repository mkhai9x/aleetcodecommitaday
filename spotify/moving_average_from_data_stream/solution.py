class MovingAverage:
    def __init__(self, size: int):
        self.current_sum = 0
        self.left = 0
        self.right = 0
        self.size = size
        self.array = []

    def next(self, val: int) -> float:
        result = 0
        if self.right - self.left < self.size:
            self.current_sum += val
            self.array.append(val)
            result = self.current_sum / len(self.array)

        else:
            self.current_sum += val
            self.current_sum -= self.array[self.left]
            self.left += 1
            self.array.append(val)
            result = self.current_sum / self.size

        self.right += 1
        return result


moving_average = MovingAverage(3)
print(moving_average.next(1))
print(moving_average.next(10))
print(moving_average.next(3))
print(moving_average.next(5))
