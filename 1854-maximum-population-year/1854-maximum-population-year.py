class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        years = [0] * 102
        for birth, death in logs:
            years[birth - 1950] += 1
            years[death - 1950] -= 1
        pref, ans = 0, [-1, -1]
        for i in range(len(years)):
            pref += years[i]
            if pref > ans[0]:
                ans = [pref, i + 1950]
                
        return ans[1]