from typing import List
from collections import Counter
# class Solution:
#     def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
#         result = []
#         used_numbers = {}
#         for number in candidates:
#             if number not in used_numbers:
#                 used_numbers[number] = 1
#             else:
#                 used_numbers[number] += 1
#         self.backtrack(candidates,target,used_numbers,0,[], result)
#         print(result)
#     def backtrack(self, candidates: List[int], target: int, used_numbers: dict[int,int], start: int, comb: List[int], result: List[List[int]]):
#         if target == 0:
#             result.append(list(comb))
#             return
#
#         for i in range(start, len(candidates)):
#             if target < candidates[i] or used_numbers[candidates[i]] == 0:
#                 continue
#             comb.append(candidates[i])
#             old_freq = used_numbers[candidates[i]]
#             used_numbers[candidates[i]] -= 1
#             self.backtrack(candidates,target-candidates[i],used_numbers,i + 1, comb,result)
#             popped_number = comb.pop()
#             used_numbers[popped_number] = old_freq
#             # del used_numbers[popped_number]
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        def backtrack(comb, remain, curr, counter, results):
            if remain == 0:
                # make a deep copy of the current combination
                #   rather than keeping the reference.
                results.append(list(comb))
                return
            elif remain < 0:
                return

            for next_curr in range(curr, len(counter)):
                candidate, freq = counter[next_curr]

                if freq <= 0:
                    continue

                # add a new element to the current combination
                comb.append(candidate)
                counter[next_curr] = (candidate, freq-1)

                # continue the exploration with the updated combination
                backtrack(comb, remain - candidate, next_curr, counter, results)

                # backtrack the changes, so that we can try another candidate
                counter[next_curr] = (candidate, freq)
                comb.pop()

        results = []  # container to hold the final combinations
        counter = Counter(candidates)
        # convert the counter table to a list of (num, count) tuples
        counter = [(c, counter[c]) for c in counter]

        backtrack(comb = [], remain = target, curr = 0,
                  counter = counter, results = results)
        print(results)
        return results

if __name__ == '__main__':
    solution = Solution()
    solution.combinationSum2([10,1,2,7,6,1,5], 8)
