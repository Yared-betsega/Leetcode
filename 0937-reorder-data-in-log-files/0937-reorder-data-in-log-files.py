class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digits = []
        letters = []
        for s in logs:
            log = s.split()
            if log[1].isdigit():
                digits.append(s)
            else:
                letters.append([log[0], log[1:]])
        sortedLetters = sorted(letters, key = lambda x: (x[1], x[0]))
        
        ans = []
        for elem, value in sortedLetters:
            ans.append([elem])
            for val in value:
                ans[-1].append(val)
                
            ans[-1] = " ".join(ans[-1])
        
        ans.extend(digits)
        

        return ans