class Solution:
    def countVowels(self, word: str) -> int:
        vowels = {"a", "e", "i", "o", "u"}
        total_count = 0
        for i in range(len(word)):
            if word[i] in vowels:
                total_count += (i+1) * (len(word) - i)
        return total_count

# time and space complexity
# time: O(n)
# space: O(1)