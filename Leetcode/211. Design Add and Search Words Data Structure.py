# https://leetcode.com/problems/design-add-and-search-words-data-structure/

class TrieNode:
    def __init__(self):
        self.nodes = {}
        self.isEnd = False
        
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        current = self.root
        for letter in word:
            if letter not in current.nodes:
                current.nodes[letter] = TrieNode()
            current = current.nodes[letter]
        current.isEnd = True

    def search(self, word, node=None, index = 0) -> bool:
        def find(node, index):
            current = node 
            for i in range(index, len(word)):
                if word[i] == '.':

                    for node in current.nodes:
                        found = find(current.nodes[node], index = i+1)
                        if found:
                            return found
                    return False
                elif word[i] in current.nodes:
                    current = current.nodes[word[i]]
                else:
                    return False

            return current.isEnd 
        
        return find(self.root, 0)



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
