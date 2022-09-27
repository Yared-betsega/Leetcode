class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        forceFromLeft = [0] * len(dominoes)
        last = -float("inf")
        for i in range(len(dominoes)):
            if dominoes[i] == ".":
                forceFromLeft[i] = i - last
            elif dominoes[i] == "R":
                last = i
            else:
                last = -float("inf")
            
        forceFromRight = [0] * len(dominoes)
        last = float("inf")
        for i in range(len(dominoes) - 1, -1, -1):
            if dominoes[i] == ".":
                forceFromRight[i] = last - i
            elif dominoes[i] == "L":
                last = i
            else:
                last = float("inf")
                
        dominoes = list(dominoes)    
        for i in range(len(dominoes)):
            if dominoes[i] == ".":
                if forceFromRight[i] < forceFromLeft[i]:
                    dominoes[i] = "L"
                elif forceFromRight[i] > forceFromLeft[i]:
                    dominoes[i] = "R"
        
        return "".join(dominoes)

# time and space complexity
# time: O(n)
# space: O(n)
