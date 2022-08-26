class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        n = str(n)
        count = Counter(n)
        i = 0
        num = "1"
        while int(num) <= 10**9:
            if len(str(num)) == len(n):
                ct = Counter(num)
                valid = True
                for j in n:
                    if count[j] != ct[j]:
                        valid = False
                if valid:
                    return True
            i += 1
            num = str(2 ** i)
            
        return False
       