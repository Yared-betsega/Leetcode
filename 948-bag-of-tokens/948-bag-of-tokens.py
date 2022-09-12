class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        if  not tokens:
            return 0
            
        tokens.sort()
        l, r = 0, len(tokens) - 1
        score = 0
        while l <= r:
            if power >= tokens[l]:
                score += 1
                power -= tokens[l]
                l += 1
            elif score >= 1 and r > l:
                score -= 1
                power += tokens[r]
                r -= 1
            else:
                break

        return score
                
# time and space complexity
# time: O(nlogn)
# space: O(1)