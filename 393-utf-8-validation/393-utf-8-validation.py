class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        i = jumpState = 0
        while i < len(data):
            rep = bin(data[i])[2:]
            binary = "0" * (8 - len(rep)) + rep
            if jumpState:
                if binary[:2] != "10":
                    return False
                jumpState -= 1
            else:
                zero = binary.find("0")
                if zero == -1 or zero == 1 or zero > 4:
                    return False
                elif zero > 0: 
                    jumpState = zero - 1
            i += 1
        return True if jumpState == 0 else False