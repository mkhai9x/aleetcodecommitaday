from heapq import heappop,heappush
class Solution:
    def frequencySort(self, s: str) -> str:
        letter_frequency = {}
        max_heap = []
        for letter in s:
            if letter not in letter_frequency:
                letter_frequency[letter] = 1
            else:
                letter_frequency[letter] += 1
        for (letter, count) in letter_frequency.items():
            heappush(max_heap, (-count, letter))
        word_list = []
        while len(max_heap) > 0:
            frequency, letter = heappop(max_heap)
            for i in range((-1) * frequency):
                word_list.append(letter)
        return "".join(word_list)
if __name__ == '__main__':
    solution = Solution()
    print(solution.frequencySort("tree"))