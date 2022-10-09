import heapq as hq
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        repo = defaultdict(int)
        for i in range(len(s)):
            repo[s[i]] = i
        ans = []
        last = -1
        bound = -1
        for i in range(len(s)):
            if repo[s[i]] > bound:
                bound = repo[s[i]]
            if i == bound:
                ans.append(bound - last)
                last = i
            
        return ans

# time and space complexity 
# time complexity = O(n + klog(k))
# k == len(set(s))
# space complexity = O(n)
                
        
            
        
        
                