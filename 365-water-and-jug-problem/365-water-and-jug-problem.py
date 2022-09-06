class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        if jug1Capacity + jug2Capacity < targetCapacity:
            return False
        def greatestCommonDevisor(x, y):
           while(y):
               x, y = y, x % y
           return x
        
        gcd = greatestCommonDevisor(jug1Capacity, jug2Capacity)
        return True if targetCapacity % gcd == 0 else False

# time and space complexity
# n = max(jug1Capacity, jug2Capacity)
# time: O(logn)
# space: O(1)
    