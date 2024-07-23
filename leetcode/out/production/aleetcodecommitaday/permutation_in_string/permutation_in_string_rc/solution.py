from typing import List

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_start,matched_pattern = 0,0
        letter_frequency = {}
        for letter in s1:
            if letter not in letter_frequency:
                letter_frequency[letter] = 0
            letter_frequency[letter] += 1

        for window_end in range(len(s2)):
            right_char = s2[window_end]
            if right_char in letter_frequency:
                letter_frequency[right_char] -= 1
                if letter_frequency[right_char] == 0:
                    matched_pattern += 1
            if matched_pattern == len(letter_frequency):
                return True
            if window_end >= len(s1) - 1:
                left_char = s2[window_start]
                if left_char in letter_frequency:
                    if letter_frequency[left_char] == 0:
                        matched_pattern -= 1
                    letter_frequency[left_char] += 1
                window_start += 1
        return False

if __name__ == '__main__':
    solution = Solution()
    solution.checkInclusion("abcdxabcde", "abcdeabcdx")