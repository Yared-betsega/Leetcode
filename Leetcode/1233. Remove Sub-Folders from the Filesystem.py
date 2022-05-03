# https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/

class TrieNode:
    def __init__(self):
        self.nodes = {}
        self.isEnd = False
        
class Trie:

    def __init__(self):
        self.root = TrieNode()
        
    def addFolder(self, word: str) -> None:
        current = self.root
        for i in range(len(word)):
            if word[i] not in current.nodes:
                current.nodes[word[i]] = TrieNode()
            current = current.nodes[word[i]]
            if current.isEnd and word[i+1] == '/':
                return
        current.isEnd = True
        current.nodes = {}
        

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = Trie()
        for cur in folder:
            trie.addFolder(cur)
            
        answer, lst = [], []
        def dfs(node, current):
            lst.append(node)
            if current.isEnd:
                answer.append("".join(lst))
            for node in current.nodes:
                dfs(node, current.nodes[node])
                
            lst.pop()
            
        dfs("", trie.root)
        return answer
            
