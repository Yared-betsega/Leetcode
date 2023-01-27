class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        wordSet = set(words)
        def dp(index, s, memo):
            if index == len(s):
                return True
            if index in memo:
                return memo[index]
            
            string = ""
            for i in range(index, len(s)):
                string += s[i]
                if string in wordSet:
                    if dp(i + 1, s, memo):
                        memo[index] = True
                        return True
            memo[index] = False
            return False
        
        answer = []
        for word in words:
            wordSet.remove(word)
            if dp(0, word, {}):
                answer.append(word)
            wordSet.add(word)
        return answer
