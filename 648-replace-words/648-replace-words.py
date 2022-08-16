class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.end=True
    
    def getMinPrefix(self, word):
        cur, prefix = self.root, ""
        for char in word:
            if char not in cur.children:
                return ""
            prefix += char
            cur = cur.children[char]
            if cur.end:
                return prefix
        
        return prefix if cur.end else ""
        
        
    
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for word in dictionary:
            trie.insert(word)
        
        words = sentence.split(" ")
        
        answer = []
        for word in words:
            prefix = trie.getMinPrefix(word)
            if len(prefix) > 0:
                answer.append(prefix)
            else:
                answer.append(word)
                
        return " ".join(answer)
        
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
