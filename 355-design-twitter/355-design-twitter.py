class Twitter:

    def __init__(self):
        self.follows = defaultdict(set)
        self.tweets = defaultdict(set)
        self.index = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].add((self.index, tweetId))
        self.index += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        cands = list(self.tweets[userId])
        for id in self.follows[userId]:
            cands.extend(self.tweets[id])
        
        cands.sort(reverse = True)
        return list(map(lambda x: x[1], cands[:10]))

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)
    
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)