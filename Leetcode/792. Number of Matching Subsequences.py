# https://leetcode.com/problems/number-of-matching-subsequences/

class TrieNode:
    def __init__(self):
        self.nodes = {}
        self.isEnd = 0
        
class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str, count) -> None:
        current = self.root
        for letter in word:
            if letter not in current.nodes:
                current.nodes[letter] = TrieNode()
            current = current.nodes[letter]
        current.isEnd = count

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        count = Counter(words)
        trie = Trie()
        for word in words:
            trie.insert(word, count[word])
            
        self.ans = 0  
        def find(node, i):
            for child in node.nodes:
                pos = s.find(child, i+1, len(s))
                if pos != -1:
                    self.ans += node.nodes[child].isEnd
                    find(node.nodes[child], pos)
                    
        find(trie.root, -1)
        return self.ans


                
        
        
