# https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        inDegrees = [0] * (n)
        outgoing = defaultdict(set)
        for frm, to in edges:
            outgoing[frm].add(to)
            inDegrees[to] += 1

        queue = deque()
        for i in range(n):
            if inDegrees[i]==0:
                queue.append(i)

        answer = defaultdict(set)
        while queue:
            frm = queue.popleft()
            for to in outgoing[frm]:
                inDegrees[to]-=1
                
                answer[to] = answer[to].union(answer[frm])
                answer[to].add(frm)
                if inDegrees[to]==0:
                    queue.append(to)
        res = []
        for i in range(n):
            res.append(sorted(answer[i]))
        return res

# time and space complexity
# time complexity = O(n**2log(n))
# space complexity = O(n)
