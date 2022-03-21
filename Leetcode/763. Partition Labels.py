
# https://leetcode.com/problems/partition-labels/

import heapq as hq
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        repo = defaultdict(list)
        for i in range(len(s)):
            repo[s[i]].append(i)
        
        pos = list(repo.items())
        heap = []
        for i in range(len(pos)):
            hq.heappush(heap, pos[i][1])
            
        cur = hq.heappop(heap)
        ans = [cur[-1] - cur[0] + 1]
        
        while heap:
            temp = hq.heappop(heap)
            if temp[0] < cur[-1]:
                if temp[-1] > cur[-1]:
                    cur[-1] = temp[-1]
                    ans[-1] = cur[-1] - cur[0] + 1
                    
            else:
                cur = temp
                ans.append(cur[-1] - cur[0] + 1)
                
        return ans

# time and space complexity 
# time complexity = O(n + klog(k))
# k == len(set(s))
# space complexity = O(n)
                
        
            
        
        
                
