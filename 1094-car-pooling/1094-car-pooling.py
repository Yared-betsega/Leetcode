class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        travel = [0] * max(map(lambda x: x[2], trips))
        
        for num, fr, to in trips:
            travel[fr] += num
            if to < len(travel):
                travel[to] -= num
                
        prefixSum = 0
        for passangers in travel:
            prefixSum += passangers
            if prefixSum > capacity:
                return False
        return True

# time and space complexity
# time: O(n)
# space: O(n)
            