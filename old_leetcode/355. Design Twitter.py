import collections
import heapq
from typing import List


class Twitter:

    def __init__(self):
        self.tweets = {}
        self.followers = {}
        self.feeds = {}
        self.limit = 10

    def postTweet(self, userId: int, tweetId: int) -> None:
        print(self.followers[userId])
        print("=================")
        for followerId in self.followers[userId]:
            maxHeap = self.tweets.setdefault(followerId, [])
            heapq.heappush(maxHeap, tweetId)
            while len(maxHeap) > self.limit:
                heapq.heappop(maxHeap)

        print(f"tweets: {self.tweets}")

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        for i in range(len(self.tweets[userId])):
            res.append(heapq.heappop(self.tweets[userId]))
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers.setdefault(followeeId, set()).add(followerId)
        print(f"followers: {self.followers}")

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followers[followeeId].remove(followerId)


if __name__ == '__main__':
    service = Twitter()
    service.follow(2, 1)
    service.follow(2, 3)
    service.follow(4, 3)
    service.follow(5, 3)
    service.postTweet(1, 1)
    service.postTweet(1, 2)
    service.postTweet(1, 3)
    service.postTweet(3, 4)
    service.postTweet(3, 5)
    service.postTweet(3, 6)
    service.postTweet(3, 7)
    service.unfollow(2, 3)

    print(service.getNewsFeed(4))

    print("++++++++++++")
    ss = set()
    ss.add(3)
    ss.add(4)
    for elem in ss:
        print(type(elem))
        print(elem)

# not optimized for reading operations. reads >> writes
class TwitterOrdinary:

    def __init__(self):
        self.tweets = {}
        self.follows = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.setdefault(userId, []).append(tweetId)

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        for followeeId in self.follows[userId]:
            for tweet in self.tweets[followeeId]:
                res.append(tweet)
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows.setdefault(followerId, set()).add(followeeId)
        print(f"followees: {self.follows}")

    def unfollow(self, followerId: int, followeeId: int) -> None:
        pass
