# https://leetcode.com/problems/implement-trie-prefix-tree/

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

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for letter in prefix:
            index = ord(letter) - ord("a")
            if not current.nodes[index]:
                return False
            current = current.nodes[index]
  
        return True


# time and space complexity for all functions
# time complexity = O(k), k = longestWord.length
# space complexity = O(n*k)
