class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        if jug1Capacity + jug2Capacity < targetCapacity:
            return False
        
#         def gcd(a, b):
#             if b == 0:
#                 return a
#             return gcd(b, a % b)
            
#         return targetCapacity % gcd(jug1Capacity,  jug2Capacity) == 0
        
        visited = set()
        def dfs(a, b):
            
            if a == targetCapacity or b == targetCapacity or a + b == targetCapacity:
                return True
            
            if (a, b) in visited:
                return False
            
            visited.add((a, b))
            fill = [(jug1Capacity, b)]
            [(a, 0), (0, b), ()]
            
            if dfs(max(0, a - (jug2Capacity - b)), min(jug2Capacity, b + a)):
                return True
            
            if dfs(min(jug1Capacity, a + b), max(0, b - (jug1Capacity - a))):
                return True
            
            if dfs(jug1Capacity, b):
                return True
                
            if dfs(a, jug2Capacity):
                return True
            
            if dfs(0, b):
                return True
            
            if dfs(a, 0):
                return True

            return False
        
        return dfs(0, 0)
            