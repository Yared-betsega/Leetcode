class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        
        graph = defaultdict(list)
        indegree = [0] * len(quiet)
        for rich, poor in richer:
            graph[rich].append(poor)
            indegree[poor] += 1
        
        queue = deque()
        for i in range(len(quiet)):
            if indegree[i] == 0:
                queue.append(i)
        answer = [i for i in range(len(quiet))]
        while queue:
            currentPerson = queue.popleft()
            for poorer in graph[currentPerson]:
                if quiet[answer[currentPerson]] < quiet[answer[poorer]]:
                    answer[poorer] = answer[currentPerson]
                indegree[poorer] -= 1
                if indegree[poorer] == 0:
                    queue.append(poorer)
        
        return answer