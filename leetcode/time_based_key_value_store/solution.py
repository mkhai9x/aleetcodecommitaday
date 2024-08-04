from collections import defaultdict


class TimeMap:
    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        key_store = self.store.get(key)
        if not key_store:
            return ""
        key_store = sorted(key_store, key=lambda x: x[1])
        low = 0
        high = len(key_store) - 1
        while low < high:
            mid = low + (high - low) // 2 + 1

            mid_value = key_store[mid]

            if mid_value[1] <= timestamp:
                low = mid
            else:
                high = mid - 1

        return key_store[low][0] if key_store[low][1] <= timestamp else ""


timeMap = TimeMap()

timeMap.set("foo", "bar", 1)
print(timeMap.get("foo", 1))
print(timeMap.get("foo", 3))
timeMap.set("foo", "bar2", 4)
print(timeMap.get("foo", 4))
print(timeMap.get("foo", 5))
