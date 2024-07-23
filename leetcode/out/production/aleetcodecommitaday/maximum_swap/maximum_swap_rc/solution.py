from typing import List
class Solution:
    def maximumSwap(self, num: int) -> int:
        num_list = list(str(num))
        potential_swap = False
        for i in range(0, len(num_list) - 1):
            if num_list[i] < num_list[i + 1]:
                potential_swap = i
                break
        if potential_swap is False:
            return num
        max_right = num_list[potential_swap]
        max_right_index = potential_swap + 1
        max_left_index = potential_swap
        for j in range(potential_swap + 1, len(num_list)):
            if num_list[j] >= max_right:
                max_right = num_list[j]
                max_right_index = j
        for k in range(potential_swap - 1, -1, -1):
            if num_list[k] < max_right:
                max_left_index = k

        num_list[max_right_index], num_list[max_left_index] = num_list[max_left_index], num_list[max_right_index]
        return int("".join(num_list))

















if __name__ == '__main__':
    solution = Solution()