class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        monotonicity = [[1, 1]] * len(security)
        inc, dec = 1, 1
        for i in range(1, len(security)):
            if security[i] <= security[i-1]:
                dec += 1
            else: 
                dec = 1
            if security[i] >= security[i-1]:
                inc += 1
            else:
                inc = 1
            monotonicity[i] = [dec, inc]
            
        good_days = []
        for i in range(len(security)):
            if i - time >= 0 and i + time <= len(security) - 1:
                if monotonicity[i][0] >= time + 1 and monotonicity[i + time][1] >= time + 1:
                    good_days.append(i)
        return good_days

# time and space complexity
# time: O(n)
# space: O(n)