from typing import List
from collections import defaultdict, Counter


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        result = []
        num_counter = Counter(nums)
        frequency_dict = defaultdict(list)
        for num, frequency in num_counter.items():
            frequency_dict[frequency].append(num)

        sorted_frequency = sorted(frequency_dict.keys())
        for each in sorted_frequency:
            sorted_nums = sorted(frequency_dict[each], reverse=True)
            for num in sorted_nums:
                result.extend([num] * each)
        return result


print(Solution().frequencySort(nums=[1, 1, 2, 2, 2, 3]))
print(Solution().frequencySort(nums=[2, 3, 1, 3, 2]))
print(Solution().frequencySort(nums=[-1, 1, -6, 4, 5, -6, 1, 4, 1]))
