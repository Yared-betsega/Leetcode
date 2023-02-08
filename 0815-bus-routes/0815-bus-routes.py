class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target: 
            return 0
        
        routes = list(map(set, routes))
        graph = defaultdict(set)
        
        for i, route1 in enumerate(routes):
            for j in range(i+1, len(routes)):
                route2 = routes[j]
                add = False
                for pos in route1:
                    if pos in route2:
                        add = True
                        break
                if add:
                    graph[i].add(j)
                    graph[j].add(i)

        visited, targets = set(), set()
        for node, route in enumerate(routes):
            if source in route: 
                visited.add(node)
            if target in route: 
                targets.add(node)

        queue = [(node, 1) for node in visited]
        for node, depth in queue:
            if node in targets: 
                return depth
            for neigh in graph[node]:
                if neigh not in visited:
                    visited.add(neigh)
                    queue.append((neigh, depth+1))
        return -1