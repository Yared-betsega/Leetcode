class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        parent = {}
        value = {}
        def find(x):
            if x == parent[x][0]:
                return parent[x]
            parentX, parentV = find(parent[x][0]) 
            parent[x] = (parentX, parentV * parent[x][1]) 
            return parent[x] 
        
        def divide(a, b):
            pa, va = find(a)  
            pb, vb = find(b)  
            return vb/va if pa == pb else -1.0   
        
        for (x, y), v in zip(equations, values):
            if x not in parent and y not in parent:
                parent[x] = (x, 1.0)
                parent[y] = (x, v)
            elif x not in parent:
                py, parentV = find(y) 
                parent[x] = (py, parentV / v)
            elif y not in parent:
                parentX, parentV = find(x)
                parent[y] = (parentX, parentV * v) 
            else:
                parentX, parentVx = find(x)
                py, parentVy = find(y)
                if parentX != py:
                    parent[py] = (parentX, parentVx * v / parentVy)
            
        return [divide(x, y) if x in parent and y in parent else -1.0 for x, y in queries]