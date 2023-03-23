class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window_start, max_letter_count, max_length = 0,0,0
        letter_frequency = {}
        for window_end in range(len(s)):
            right_letter = s[window_end]
            if right_letter not in letter_frequency:
                letter_frequency[right_letter] = 0

            letter_frequency[right_letter] += 1
            # we find the most frequent letter in our current window
            max_letter_count = max(max_letter_count, letter_frequency[right_letter])

            # if our maximum occuring letter in our current window  + k is less than the window length, it means we have to replace too much
            while window_end - window_start + 1 - max_letter_count > k:
                left_char = s[window_start]
                letter_frequency[left_char] -= 1
                max_letter_count = max(max_letter_count, letter_frequency[left_char])
                window_start += 1
            max_length = max(max_length, window_end - window_start + 1)

        return max_length


if __name__ == '__main__':
    solution = Solution()
    assert solution.characterReplacement("ABAB", 2) == 4
    assert solution.characterReplacement("AABABBA", 1) == 4

