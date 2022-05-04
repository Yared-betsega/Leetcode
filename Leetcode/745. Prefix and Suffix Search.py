# https://leetcode.com/problems/prefix-and-suffix-search/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
        self.index = 0
        
class Trie:

    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str, index: int) -> None:
        current = self.root
        for letter in word:
            if letter not in current.children:
                current.children[letter] = TrieNode()
            current = current.children[letter]
        current.isEnd = True
        current.index = index
        
    def search(self, prefix, suffix) -> bool:
        
        current = self.root
        lst = []
        for letter in prefix:
            if letter not in current.children:
                return [-1, -1]
            lst.append(letter)
            current = current.children[letter]
            
        self.maxim = [-1, None]
        def dfs(m, current):
            if current.isEnd:
                cur = lst[::-1]
                notValid = False
                for i in range(len(suffix)):
                    if cur[i] != suffix[i]:
                        notValid = True
                        break
                if not notValid:
                    self.maxim = max([current.index, cur], self.maxim)
                        
            for node in current.children:
                lst.append(node)
                dfs(node, current.children[node])
                
            lst.pop()
            
        dfs(letter, current)
        return self.maxim
        

class WordFilter:

    def __init__(self, words: List[str]):
        self.words = words
        self.trie = Trie()   
        for i in range(len(words)):
            self.trie.insert(words[i], i)
        
    def f(self, prefix: str, suffix: str) -> int:
        
        return self.trie.search(prefix, suffix[::-1])[0]
        
                

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)
