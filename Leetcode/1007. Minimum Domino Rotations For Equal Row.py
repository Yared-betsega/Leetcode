
# https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/

import heapq as hq
class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        
        def swap(tops, bottoms):
            
            topsRep, heap = Counter(tops).items(), []
            
            for val, rep in topsRep:
                hq.heappush(heap, [-1 * rep, val])

            while heap:
                highFreq, counter, loopBroke = hq.heappop(heap)[1], 0, False
                for i in range(len(tops)):
                    if tops[i] != highFreq:
                        if bottoms[i] == highFreq:
                            counter += 1
                        else:
                            loopBroke = True
                            break
                if not loopBroke:
                    return counter
            return -1
        
        forTop, forBottom = swap(tops, bottoms), swap(bottoms, tops)
        
        if forTop == -1:
            return forBottom
        elif forBottom == -1:
            return forTop
        else:
            return min(forTop, forBottom)

# time and space complexity
# time complexity = O(n**2)
# space complexity = O(n)
