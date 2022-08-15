class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp = [[1]]
        
        def get(lst, index):
            return lst[index] if 0<=index<len(lst) else 0
        
        def row(dp):
            if len(dp) == numRows:
                return dp

            last = dp[-1]
            temp = []
            for i in range(len(last)+1):
                temp.append(get(last, i-1) + get(last, i))
            
            dp.append(temp)
            
            return row(dp)
        
        return row(dp)
    
# time and space complexity
# time complexity = O(n**2)
# space complexity = O(n)
                