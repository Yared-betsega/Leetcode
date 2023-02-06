class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        
        words.sort(key=lambda x: len(x))
        dp = Counter()
        for word in words:
            dp[word] = 0
            for i in range(len(word)):
                dp[word] = max(dp[word[:i] + word[i+1:]], dp[word])
            dp[word] += 1
        
        return max(dp.values())