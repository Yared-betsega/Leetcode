class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        dp = [1]
        
        def get(lst, index):
            return lst[index] if 0<=index<len(lst) else 0
        
        def row(dp):
            if len(dp) == rowIndex+1:
                return dp
            temp = []
            for i in range(len(dp)+1):
                temp.append(get(dp, i-1) + get(dp, i))
            
            dp = temp
            return row(dp)
        
        return row(dp)
    
# time and space complexity
# time complexity = O(n**2)
# space complexity = O(n), n == rowIndex