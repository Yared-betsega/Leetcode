class Solution:
    def kthGrammar(self, n, k):
        if n == 1:
            return 0
        else:
            upper = self.kthGrammar(n-1, k//2 + k % 2)
            if upper == 1:
                return 0 if k % 2 == 0 else 1
            return 1 if k % 2 == 0 else 0
