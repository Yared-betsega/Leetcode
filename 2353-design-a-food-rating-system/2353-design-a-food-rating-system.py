class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.rating = {}
        self.cuisines = {}
        self.removed = defaultdict(set)
        self.highest = defaultdict(list)
        for i in range(len(foods)):
            self.rating[foods[i]] = ratings[i]
            self.cuisines[foods[i]] = cuisines[i]
            heappush(self.highest[cuisines[i]], (-ratings[i], foods[i]))
            
    def changeRating(self, food: str, newRating: int) -> None:
        self.removed[self.cuisines[food]].add((-self.rating[food], food))
        heappush(self.highest[self.cuisines[food]], (-newRating, food))
        self.rating[food] = newRating
        if (-newRating, food) in self.removed[self.cuisines[food]]:
            self.removed[self.cuisines[food]].remove((-newRating, food))
        
    def highestRated(self, cuisines: str) -> str:
        while self.highest and self.highest[cuisines][0] in self.removed[cuisines]:
            heappop(self.highest[cuisines])
        return self.highest[cuisines][0][1]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)