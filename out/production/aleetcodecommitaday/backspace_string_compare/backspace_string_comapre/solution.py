class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_right, t_right = len(s) - 1, len(t) - 1
        while (s_right >= 0 or t_right >= 0):
            s_valid = self.get_next_valid_character(word=s,index=s_right)
            t_valid = self.get_next_valid_character(word=t, index=t_right)
            if s_valid < 0 and t_valid < 0:
                return True
            if s_valid < 0 or t_valid < 0:
                return False
            if s[s_valid] != t[t_valid]:
                return False
            s_right = s_valid - 1
            t_right = t_valid - 1
        return True
    def get_next_valid_character(self, word: str, index: int):
        backspace_counter = 0
        while index >= 0:
            if word[index] == '#':
                backspace_counter += 1
            elif backspace_counter > 0:
                backspace_counter -= 1
            else:
                break
            index -= 1

        return index

if __name__ == '__main__':
    solution = Solution()
    print(solution.backspaceCompare("nzp#o#g","b#nzp#o#g"))