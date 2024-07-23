class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_string = ""
        for i in s:
            if i.isalnum():
                clean_string += i.lower()
        left = 0
        right = len(clean_string) - 1
        while left < right:
            if clean_string[left] != clean_string[right]:
                return False
            left += 1
            right -= 1
        return True


s = "A0 man, a plan, a canal: Panama"
print(Solution().isPalindrome(s))
