class Solution:
    def candy(self, ratings: List[int]) -> int:
        
        isValid = lambda x:0<=x<len(ratings)
        answer = [1] * len(ratings)
        
        for i in range(len(ratings)):
            temp = i
            if isValid(temp-1) and ratings[temp-1] < ratings[temp] and answer[temp-1]>= answer[temp]:
                answer[temp]  = answer[temp-1] + 1
            
            if (isValid(temp+1) and ratings[temp+1] >= ratings[temp]) or temp == len(ratings)-1:
                while isValid(temp-1) and ratings[temp-1] > ratings[temp] and answer[temp-1] <= answer[temp]:
                    answer[temp-1] = answer[temp] + 1
                    temp -= 1
                    
        return sum(answer)
    
# time and space complexity 
# time complexity = O(n)
# space complexity = O(n)
                
                
        
