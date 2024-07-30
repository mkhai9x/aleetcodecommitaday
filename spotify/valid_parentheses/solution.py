class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open = {"(", "{", "["}
        pair = {")": "(", "}": "{", "]": "["}
        for each in s:
            if each in open:
                stack.append(each)
            else:
                match = pair[each]
                if len(stack) != 0 and stack[-1] == match:
                    stack.pop()

                else:
                    return False
        return len(stack) == 0


s = "(])"

print(Solution().isValid(s))
