# https://leetcode.com/problems/fruit-into-baskets/

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        types = []
        l = r = 0
        ans = 0
        while r < len(fruits):
            if fruits[r] not in types:
                if len(types) < 2:
                    types.append(fruits[r])
                else:
                    ans = max(ans, r-l)
                    l = r-1
                    while fruits[l] == fruits[r-1]:
                        l -= 1
                    l += 1
                    types = [fruits[l], fruits[r]]
            r += 1
        ans = max(ans, r-l)
        return ans

# time and space complexity 
# time coplexity = O(n)
# space complexity = O(1)
            
                    
        
            
        
            
