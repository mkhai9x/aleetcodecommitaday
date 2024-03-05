class Solution:
    def isHappy(self, n: int) -> bool:
        fast,slow = n,n
        while True:
            slow = self.calculate_happy(slow)
            fast = self.calculate_happy(self.calculate_happy(fast))
            if fast == slow:
                break
        return slow == 1
    def calculate_happy(self,n):
        sum = 0
        while n > 0:
            digit = n % 10
            sum += digit * digit
            n //= 10
        return sum


if __name__ == '__main__':
    solution = Solution()
    print(solution.isHappy(19)) # should be true
    print(solution.isHappy(23)) # should be true
    print(solution.isHappy(12)) # should be false