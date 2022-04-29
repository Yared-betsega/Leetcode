# import heapq as hq
# class Solution:
#     def topKFrequent(self, words: List[int], k: int) -> List[int]:
#         repo = Counter(words).items()
#         repo = list(repo)
#         for i in range(len(repo)):
#             repo[i] = -1 * repo[i][1], repo[i][0]
            
#         hq.heapify(repo)
        
#         answer = []
#         for i in range(k):
#             seq = hq.heappop(repo)
#             answer.append(seq[1])
#         return answer

# space time complexity
# time complexity = O( n + klog(n) )
# space complexity O(1)


# Using Trie to get the count of each number
class TrieNode:
    def __init__(self):
        self.nodes = [None] * 26
        self.isEnd = False
        
class Trie:

    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        current = self.root
        for letter in word:
            index = ord(letter) - ord("a")
            if not current.nodes[index]:
                current.nodes[index] = TrieNode()
            current = current.nodes[index]
        current.isEnd = True
        
    def search(self, word: str) -> bool:
        current = self.root
        for letter in word:
            index = ord(letter) - ord("a")
            if not current.nodes[index]:
                return False
            current = current.nodes[index]
  
        return current and current.isEnd

class Solution:
    def topKFrequent(self, words: List[int], k: int) -> List[int]:
        repetition = defaultdict(int)
        trie = Trie()
        for word in words:
            if not trie.search(word):
                trie.insert(word)
            repetition[word] += 1
        heap = []
        for word, rep in repetition.items():
            heapq.heappush(heap, (-1*rep, word))
        answer = []
        for i in range(k):
            seq = heapq.heappop(heap)
            answer.append(seq[1])
        return answer

        
                
