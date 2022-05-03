# https://leetcode.com/problems/longest-word-in-dictionary/

class TrieNode:
    def __init__(self):
        self.nodes = {}
        self.isEnd = False
        
class Trie:

    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        current = self.root
        for letter in word:
            if letter not in current.nodes:
                current.nodes[letter] = TrieNode()
            current = current.nodes[letter]
        current.isEnd = True
    
    def search(self, word: str) -> bool:
        current = self.root
        for letter in word:
            if letter not in current.nodes:
                return False
            current = current.nodes[letter]
  
        return current.isEnd 


class Solution:
    def longestWord(self, words: List[str]) -> str:
        heap = []
        trie = Trie()
        for word in words:
            heapq.heappush(heap, (-1*len(word), word))
            trie.insert(word)
        
        answer = []
        while heap:
            notFound = False
            cur = heapq.heappop(heap)[1]
            for i in range(1, len(cur)):
                if not trie.search(cur[:i]):
                    notFound = True
                    break
            if not notFound:
                return cur
        
        return ""
                    
