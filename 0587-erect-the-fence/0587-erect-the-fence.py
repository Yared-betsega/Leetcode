class Settlement:
    @staticmethod
    def long_signum(i):
        return int(((i >> 63) | (-i >> 63)))
    
class P():
    x = 0
    y = 0

    def __init__(self, x,  y):
        self.x = x
        self.y = y

    def add(self, p):
        return P(self.x + p.x, self.y + p.y)

    def sub(self, p):
        return P(self.x - p.x, self.y - p.y)

    def dot(self, p):
        return self.x * p.x + self.y * p.y

    def det(self, p):
        return self.x * p.y - self.y * p.x

    def compareTo(self, o):
        comp = Settlement.long_signum(self.x - o.x)
        if (comp != 0):
            return comp
        return Settlement.long_signum(self.y - o.y)

    def toString(self):
        return self.x, (self.y)

    
class Solution:
    def outerTrees(self, x: List[List[int]]) -> List[List[int]]:
        def convexHull(ps):
            n = len(ps)
            k = 0
            if (n <= 1):
                return ps
            qs = [None] * (n * 2)
            i = 0
            while (i < n):
                while (k > 1 and qs[k - 1].sub(qs[k - 2]).det(ps[i].sub(qs[k - 1])) < 0):
                    k -= 1
                qs[k] = ps[i]
                k += 1
                i += 1
            i = n - 2
            t = k
            while (i >= 0):
                while (k > t and qs[k - 1].sub(qs[k - 2]).det(ps[i].sub(qs[k - 1])) < 0):
                    k -= 1
                qs[k] = ps[i]
                k += 1
                i -= 1
            
            # print( list(map(lambda p: [p.x, p.y], qs[:k-1])))
            res = qs[:k-1]
            return res
        x.sort()
        n = len(x)
        ps = [None] * (n)
        i = 0
        while (i < n):
            ps[i] = P(x[i][0], x[i][1])
            i += 1
        ps.sort(key=cmp_to_key(P.compareTo))
        res = convexHull(ps)
        return set(map(lambda p: (p.x, p.y), res))