class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        if jug1Capacity + jug2Capacity < targetCapacity:
            return False
        
        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a % b)
            
        return targetCapacity % gcd(jug1Capacity,  jug2Capacity) == 0
    