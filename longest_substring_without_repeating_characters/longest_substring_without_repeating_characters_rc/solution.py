from typing import List

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window_start = 0
        letter_frequency = {}
        max_length = 0
        window_length = 0
        for window_end in range(len(s)):
            if s[window_end] not in letter_frequency:
                letter_frequency[s[window_end]] = 1
            else:
                letter_frequency[s[window_end]] += 1
                max_length = max(max_length, window_length)
                while (window_start < window_end and letter_frequency[s[window_end]] > 1):
                    letter_frequency[s[window_start]] -= 1
                    if letter_frequency[s[window_start]] == 0:
                        del letter_frequency[s[window_start]]
                    window_start += 1
                    window_length -= 1
            window_length += 1

        max_length = max(window_length,max_length)
        return max_length













if __name__ == '__main__':
    solution = Solution()
    assert solution.lengthOfLongestSubstring('abcabcbb') == 3
    assert solution.lengthOfLongestSubstring('bbbbb') == 1
    assert solution.lengthOfLongestSubstring('pwwkew') == 3
    assert solution.lengthOfLongestSubstring(' ') == 1
    assert solution.lengthOfLongestSubstring('aab') == 2
