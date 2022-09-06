class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        mapped = []
        for i in range(len(values)):
            mapped.append([values[i], labels[i]])
        mapped.sort(reverse = True)
        
        count = defaultdict(int)
        ans = used = 0
        for value, label in mapped:
            if used == numWanted:
                break
            if count[label] < useLimit:
                count[label] += 1
                ans += value
                used += 1
        return ans