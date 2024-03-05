class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        letter_frequency = {}
        window_start, max_length = 0,0
        for window_end in range(len(s)):
            right_char = s[window_end]
            if right_char not in letter_frequency:
                letter_frequency[right_char] = 0
            letter_frequency[right_char] += 1
            while(window_start < window_end and len(letter_frequency) > 2):
                left_char = s[window_start]
                letter_frequency[left_char] -= 1
                if letter_frequency[left_char] == 0:
                    del letter_frequency[left_char]
                window_start += 1

            max_length = max(max_length, window_end-window_start + 1)
        return max_length