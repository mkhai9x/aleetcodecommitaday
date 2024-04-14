
from typing import List


class Solution:
  def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    anagram_groups = {}
    for word in strs:
      sorted_word = ''.join(sorted(word))
      try:
        anagram_groups[sorted_word].append(sorted_word)
      except:
        anagram_groups[sorted_word] = [sorted_word]
    return anagram_groups.values()
