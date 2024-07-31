from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operator = {"+", "-", "*", "/"}
        stack = []
        for i in tokens:
            if i not in operator:
                stack.append(i)
            else:
                first_number = int(stack.pop())
                second_number = int(stack.pop())

                result = 0
                if i == "+":
                    result = first_number + second_number
                elif i == "-":
                    result = second_number - first_number
                elif i == "*":
                    result = first_number * second_number
                elif i == "/":
                    result = second_number / first_number
                stack.append(result)

        return int(stack[0])


tokens = ["2", "1", "+", "3", "*"]

tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]

tokens = ["4", "13", "5", "/", "+"]
print(Solution().evalRPN(tokens=tokens))
