# https://leetcode.com/problems/short-encoding-of-words/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
        
class Trie:

    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        current = self.root
        for letter in word:
            if letter not in current.children:
                current.children[letter] = TrieNode()
            current = current.children[letter]
        current.isEnd = True

        
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        trie = Trie()
        for word in words:
            trie.insert(word[::-1])
        
        self.ans = 0
        def dfs(node, current, path):
            if node != "":
                path.append(node)
                
            if current.isEnd and len(current.children) == 0:
                self.ans += (len(path) + 1)
                
            for child in current.children:
                dfs(child, current.children[child], path)
            
            if path:
                path.pop()
        
        dfs("", trie.root, [])
        return self.ans
                
