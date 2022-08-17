class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        words = set(wordDict)
        answer = []
        def dp(index, sentence):
            if index == len(s):
                answer.append(" ".join(sentence))
            
            string = ""
            for i in range(index, len(s)):
                string += s[i]
                if string in words:
                    copy = sentence.copy()
                    copy.append(string)
                    dp(i + 1, copy)
                        
        dp(0, [])
        return answer