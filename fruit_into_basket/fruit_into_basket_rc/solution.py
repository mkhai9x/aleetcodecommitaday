from typing import List

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fruit_counter = {}
        window_start = 0
        fruit_count = 0

        for window_end in range(len(fruits)):
            fruit = fruits[window_end]
            if fruit not in fruit_counter:
                fruit_counter[fruit] = 1
            else:
                fruit_counter[fruit] += 1
            if len(fruit_counter) > 2:
                while window_start < window_end and len(fruit_counter) > 2:
                    left_fruit = fruits[window_start]
                    fruit_counter[left_fruit] -= 1
                    if fruit_counter[left_fruit] == 0:
                        del fruit_counter[left_fruit]
                    window_start += 1
            fruit_count = max(fruit_count, window_end - window_start + 1)

        return fruit_count

if __name__ == '__main__':
    solution = Solution()
    print(solution.totalFruit([1,2,1]))
    print(solution.totalFruit([0,1,2,2]))
    print(solution.totalFruit([1,2,3,2,2]))
    print(solution.totalFruit([3,3,3,1,2,1,1,2,3,3,4]))
    print(solution.totalFruit([0,1,2]))