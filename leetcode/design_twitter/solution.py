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
        most_recent = []
        followers = self.followers[userId]
        followers.add(userId)
        for follower in followers:
            count = 0
            i = len(self.tweet[follower]) - 1
            while i >= 0 and count < 10:
                most_recent.append(self.tweet[follower][i])
                count += 1
                i -= 1
        most_recent = heapq.nsmallest(10, most_recent)
        most_recent = sorted(most_recent)
        followers.remove(userId)
        return [each[1] for each in most_recent]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)
