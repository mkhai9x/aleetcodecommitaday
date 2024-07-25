class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        tracking_table = set()
        longest = 0
        while right < len(s):
            if s[right] not in tracking_table:
                tracking_table.add(s[right])
                longest = max(longest, right - left + 1)

                right += 1
            else:
                while s[right] in tracking_table:
                    tracking_table.remove(s[left])
                    left += 1
        return longest


s = "abcabcbb"
s = "sssssss"
print(Solution().lengthOfLongestSubstring(s))
