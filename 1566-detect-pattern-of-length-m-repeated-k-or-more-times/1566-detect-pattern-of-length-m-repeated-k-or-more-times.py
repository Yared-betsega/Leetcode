class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        count = defaultdict(int)
        
        for i in range(len(arr)):
            cur = arr[i:i + m]
            count = 1
            temp = i + m
            while temp + m <= len(arr) and arr[temp: temp + m] == cur:
                count += 1
                temp += m
                
            if count >= k:
                return True
            
        return False