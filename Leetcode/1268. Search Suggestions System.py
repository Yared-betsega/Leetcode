class TrieNode:
    def __init__(self):
        self.nodes = {}
        self.isEnd = False
        
class Trie:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        current = self.root
        for letter in word:
            if letter not in current.nodes:
                current.nodes[letter] = TrieNode()
            current = current.nodes[letter]
        current.isEnd = True

    def starts_with(self, word) -> bool:
        current = self.root
        lst = []
        for letter in word:
            if letter not in current.nodes:
                return []
            lst.append(letter)
            current = current.nodes[letter]
            
        heap = []
        def dfs(m, current):
            if current.isEnd:
                heapq.heappush(heap, ''.join(lst))
                
            for node in current.nodes:
                lst.append(node)
                dfs(node, current.nodes[node])
                
            lst.pop()
            
        dfs(letter, current)
        return heap


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        for product in products:
            trie.addWord(product)
            
        answer,temp, s = [], [], ""
        for letter in searchWord:
            s += letter
            heap = trie.starts_with(s)
            
            for i in range(3):
                if not heap:
                    break
                temp.append(heapq.heappop(heap))
                
            answer.append(temp)
            temp = []
            
        return answer
