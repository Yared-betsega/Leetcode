class Solution:
    
    def reverse(self, binary):
        return binary[::-1]
        
    def invert(self, binary):
        lst = ""
        for i in range(len(binary)):
            if binary[i] == "0":
                lst += "1"
            else:
                lst += "0"
        return lst
      
    store = {}
    def helper(self, n):
        if n == 1:
            return "0"
        else:
            if n not in self.store:
                x = self.helper(n-1) + "1" + self.reverse(self.invert(self.helper(n-1)))
                self.store[n] = x
            return self.store[n]
    
    def findKthBit(self, n: int, k: int) -> str:
        createBinary = self.helper(n)
        return createBinary[k-1]
