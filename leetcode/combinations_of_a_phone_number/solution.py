from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {
            "1": [],
            "2": ["A", "B", "C"],
            "3": ["D", "E", "F"],
            "4": ["G", "H", "I"],
            "5": ["J", "K", "L"],
            "6": ["M", "N", "O"],
            "7": ["P", "Q", "R", "S"],
            "8": ["T", "U", "V"],
            "9": ["W", "X", "Y", "Z"],
            "*": [],
            "0": ["+"],
            "#": [],
        }

        result = []

        def dfs(curr, curr_index):
            if len(curr) == len(digits):
                if len(curr) != 0:
                    result.append("".join(curr))
                return

            for char in phone[digits[curr_index]]:
                curr.append(char.lower())
                dfs(curr, curr_index + 1)
                curr.pop()

        dfs([], 0)
        return result


digits = "34"
print(Solution().letterCombinations(digits))
