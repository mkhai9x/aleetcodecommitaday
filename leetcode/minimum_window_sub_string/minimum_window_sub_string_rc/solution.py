from collections import Counter
from typing import List

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dict_t = Counter(t) # keeps track of the frequency of the letters in t
        windows_count = {} # keeps track of the characters in the current window
        window_left = 0
        t_length = len(dict_t)
        window_t_substring_len = 0
        ans = (float("inf"), None, None) # holds the length of the window, start of the window and end of the window
        for window_right in range(len(s)):
            right_char = s[window_right]
            windows_count[right_char] = windows_count.get(right_char,0) + 1
            if right_char in dict_t and windows_count[right_char] == dict_t[right_char]:
                window_t_substring_len += 1
            while window_left <= window_right and t_length == window_t_substring_len: # ensure that our window left never croses our right window , additionally the current window has the substring of t
                left_char = s[window_left]
                if window_right - window_left + 1 < ans[0]:
                    ans = (window_right - window_left + 1, window_left, window_right)

                windows_count[left_char] -= 1
                if left_char in dict_t and windows_count[left_char] < dict_t[left_char]:
                    window_t_substring_len -= 1
                window_left += 1


        return "" if ans[0] == float("inf") else s[ans[1]:ans[2] + 1]










if __name__ == '__main__':
    solution = Solution()

    print(solution.minWindow("ADOBECODEBANC", "ABC"))