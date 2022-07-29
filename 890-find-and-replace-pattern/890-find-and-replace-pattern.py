class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        answer = []
        for word in words:
            mapping, taken, valid = {}, set(), True
            for i in range(len(word)):
                if pattern[i] in mapping:
                    if mapping[pattern[i]] != word[i]:
                        valid = False
                        break
                else:
                    if word[i] in taken:
                        valid = False 
                        break
                    mapping[pattern[i]] = word[i]
                    taken.add(word[i])
            if valid:
                answer.append(word)
        return answer

# time and space complexity
# n = len(words)
# m = len(words[i])
# time: O(nm)
# space: O(nm)
                