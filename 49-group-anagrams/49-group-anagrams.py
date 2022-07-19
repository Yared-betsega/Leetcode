class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        for st in strs:
            group[tuple(sorted(st))].append(st)
        return group.values()

# time and space complexity
# n = len(strs)
# m = len(strs[i])
# time: O(nmlog(m))
# space: O(n)