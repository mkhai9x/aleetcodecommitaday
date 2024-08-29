from collections import defaultdict
import heapq
from typing import List


class Twitter:
    def __init__(self):
        self.count = 0  # to represent the time
        self.tweet = defaultdict(list)
        self.followers = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet[userId].append((self.count - 1, tweetId))
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        result = []
        min_heap = []
        followers = self.followers[userId]
        followers.add(userId)

        # loop through all the followers a
        for follower in followers:
            if follower in self.tweet:
                index = len(self.tweet[follower]) - 1
                count, tweet = self.tweet[follower][index]
                min_heap.append([count, tweet, follower, index - 1])

        heapq.heapify(min_heap)
        while min_heap and len(result) < 10:
            count, tweet, follower, index = heapq.heappop(min_heap)
            result.append(tweet)

            if index >= 0:
                count, tweet = self.tweet[follower][index]
                heapq.heappush(min_heap, [count, tweet, follower, index - 1])
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)
