class Solution:
    def convertToTitle(self, n: int) -> str:
        lookup = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        title = []
        
        while n:
            n, rem = divmod(n - 1, 26)
            title.append(lookup[rem])
            
        return "".join(title[::-1])