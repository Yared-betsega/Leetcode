class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        current_index = defaultdict(int)
        cur = 0
        for i in range(len(s) + 1):
            if i == len(s) or s[i] != s[cur]:
                length_of_chars = i - cur
                temp = []
                for word in words:
                    if current_index[word] < len(word) and word[current_index[word]]==s[cur]:
                        count = float("inf")
                        for j in range(current_index[word], len(word)+1):
                            if j == len(word) or word[j] != word[current_index[word]]:
                                count = j - current_index[word]
                                current_index[word] = j
                                break
                        if i == len(s) and current_index[word] < len(word):
                            continue
                        if length_of_chars <= 2:
                            if count == length_of_chars:
                                temp.append(word)
                        else:
                            if count <= length_of_chars:
                                temp.append(word)
                words = temp
                cur = i
        return len(words)