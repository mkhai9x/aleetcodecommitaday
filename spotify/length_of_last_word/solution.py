class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        i = len(s) - 1

        while i >= 0:
            if s[i] == " ":
                break
            i -= 1

        return len(s) - 1 - i
