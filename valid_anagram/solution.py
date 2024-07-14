from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counter = Counter(s)
        t_counter = Counter(t)
        if set(s_counter.keys()) != set(t_counter.keys()):
            return False
        for s_char in s_counter:
            if s_char not in t_counter.keys():
                return False
            if s_counter[s_char] != t_counter[s_char]:
                return False
        return True
