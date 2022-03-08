class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        if n == 0:
            return True
        
        isValid = lambda x : 0 <= x < len(flowerbed)
        
        for i in range(len(flowerbed)):
            if flowerbed[i] != 1:
                if isValid(i-1) and flowerbed[i-1] == 1:
                    continue
                if isValid(i+1) and flowerbed[i+1] == 1:
                    continue
                
                flowerbed[i] = 1
                n -= 1
                if n == 0:
                    return True
                
        return False

# time and space complexity 
# time complexity = O(n)
# space complexity = O(1)
            
                
                    
