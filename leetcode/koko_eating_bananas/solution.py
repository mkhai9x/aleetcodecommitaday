from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        while low < high:
            mid = low + (high - low) // 2
            needed_hours = 0
            print(f"mid: {mid}")
            for pile in piles:
                if (pile % mid) != 0:
                    needed_hours = needed_hours + pile // mid + 1
                else:
                    needed_hours = needed_hours + pile // mid
            print(f"needed_hours: {needed_hours}")
            if needed_hours <= h:
                high = mid
            else:
                low = mid + 1
        return high


piles = [3, 6, 7, 11]

piles = [30, 11, 23, 4, 20]

h = 6

print(Solution().minEatingSpeed(piles, h))
