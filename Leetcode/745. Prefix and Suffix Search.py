# https://leetcode.com/problems/prefix-and-suffix-search/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
        self.indices = defaultdict(int)
        
class Trie:

    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str, index: int) -> None:
        current = self.root
        for letter in word:
            if letter not in current.children:
                current.children[letter] = TrieNode()
            current = current.children[letter]
            current.indices[word] = max(current.indices[word], index)
        
    def search(self, prefix) -> bool:
        
        current = self.root
        for letter in prefix:
            if letter not in current.children:
                return []
            current = current.children[letter]
        return set(current.indices.values())
    
class WordFilter:

    def __init__(self, words: List[str]):
        self.words = words
        self.triePref = Trie()   
        self.trieSuf = Trie()
        for i in range(len(words)):
            self.triePref.insert(words[i], i)
            self.trieSuf.insert(words[i][::-1], i)
        
    def f(self, prefix: str, suffix: str) -> int:
        pref = self.triePref.search(prefix)
        suf = self.trieSuf.search(suffix[::-1])
        if not pref or not suf:
            return -1
        
        ans  = -float("inf")
        for i in pref:
            if i in suf:
                ans = max(ans, i)
        return ans                

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)
        
