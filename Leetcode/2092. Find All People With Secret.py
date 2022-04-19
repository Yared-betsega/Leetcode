class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        
        # Union Find Solution
        def find_set(i, t):
            if i == children[t][i]:
                return i
            children[t][i] = find_set(children[t][i], t)
            return children[t][i]
        
        def union_sets(i, j, t):
            a = find_set(i, t)
            b = find_set(j, t)
            if a!=b:
                if a in heard:
                    children[t][b] = a
                else:
                    children[t][a] = b
                    
        meetings.sort(key = lambda x:x[2])
        
        children = defaultdict(dict)
        heard = set([0, firstPerson])
        
        # Create the graph
        for p1, p2, t in meetings:
            children[t][p1] = p1
            children[t][p2] = p2
            
        # union all meetingst that occur at the same time
        for p1, p2, t in meetings:
            union_sets(p1, p2, t)
        
        # Check if one of the two persons heard the secret then spread the secret
        for p1, p2, t in meetings:
            if p1 in heard and p2 not in heard:
                ch = find_set(p2, t)
                for k, v in children[t].items():
                    if find_set(k,t) == ch:
                        heard.add(k)
                        
            if p2 in heard and p1 not in heard:
                ch = find_set(p1, t)
                for k, v in children[t].items():
                    if find_set(k,t) == ch:
                        heard.add(k)
                
        return heard
            
            
                    
        
        
        
