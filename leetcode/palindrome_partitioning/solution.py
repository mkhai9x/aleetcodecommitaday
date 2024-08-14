from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        def is_valid_palindrome(start, end):
            while start < end:
                if s[start] == s[end]:
                    start += 1
                    end -= 1
                else:
                    return False
            return True

        def backtrack(curr, curr_index):
            if curr_index == len(s):
                result.append(curr[:])

            for i in range(curr_index, len(s)):
                if is_valid_palindrome(curr_index, i):
                    curr.append(s[curr_index : i + 1])
                    backtrack(curr, i + 1)
                    curr.pop()

        backtrack([], 0)
        return result


s = "geek"
print(Solution().partition(s))
