class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        count_words2 = defaultdict(int)
        for word in words2:
            count = Counter(word)
            for i in count:
                count_words2[i] = max(count_words2[i], count[i])
        answer = []
        for word in words1:
            count_word = Counter(word)
            for i in count_words2:
                if count_words2[i] > count_word[i]:
                    break
            else:
                answer.append(word)
        
        return answer