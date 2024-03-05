from typing import List


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        char_frequency = {}
        window_start,max_length = 0,0
        for window_end in range(len(s)):
            right_char = s[window_end]
            if right_char not in char_frequency:
                char_frequency[right_char] = 1
            else:
                char_frequency[right_char] += 1

            while len(char_frequency) > k:
                # shrink the window here by moving window_start up
                char_frequency[s[window_start]] -= 1
                if char_frequency[s[window_start]] == 0:
                    del char_frequency[s[window_start]]
                window_start += 1
            max_length = max(max_length, window_end - window_start + 1)
        return  max_length

if __name__ == '__main__':
    solution = Solution()

    assert solution.lengthOfLongestSubstringKDistinct("eceba", 2) == 3