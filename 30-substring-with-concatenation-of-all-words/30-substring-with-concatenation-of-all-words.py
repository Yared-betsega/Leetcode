class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        len_of_word_in_words = len(words[0])
        concatination_length = len(words) * len_of_word_in_words
        count = Counter(words)
        i, ans = 0, []
        while i + concatination_length <= len(s):
            added = count.copy()
            c, st, isConcatination = 1, "", True
            for j in range(i, i + concatination_length):
                st += s[j]
                if c % len_of_word_in_words == 0:
                    if st in added and added[st] > 0:
                        added[st] -= 1
                        st = ""
                    else:
                        isConcatination = False
                        break
                c += 1
            if isConcatination:
                ans.append(i)
            i += 1
        return ans

# time and space complexity
# n = len(s)
# m = len(words)
# l = len(words[i])
# time: O(lnm)
# space: O(lnm)
        