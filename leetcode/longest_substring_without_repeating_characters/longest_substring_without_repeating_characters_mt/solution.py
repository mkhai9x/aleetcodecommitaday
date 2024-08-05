class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Using slicing window technique
        we expand the right pointer when there is no duplicate and once we see a duplicated, we reduce the width of the window by imcrementing the left pointer
        until the current duplicate not in the tracked set, while we reduce the window, we remove those characters out of the set
        """

        track_set = set()
        left, right = 0, 0
        longest_substring = 0
        while right < len(s):
            while s[right] in track_set:
                track_set.remove(s[left])
                left += 1
            track_set.add(s[right])
            current_length = right - left + 1
            longest_substring = max(longest_substring, current_length)
            right += 1
        return longest_substring


s = "abcabcbb"
s = "aaaaaa"

print(Solution().lengthOfLongestSubstring(s))
