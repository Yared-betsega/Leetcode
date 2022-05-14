# https://leetcode.com/problems/word-ladder/

#Simple Breadth First search Solution
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        net = defaultdict(set)
        words = set(wordList)
        words.add(beginWord)
        alph = list(string.ascii_lowercase)
        
        for word in words:
            lst = []
            for i in range(len(word)):
                temp = word
                for j in alph:
                    temp = list(temp)
                    temp[i] = j
                    temp = "".join(temp)
                    if temp in words and temp != word:
                        net[word].add(temp)
                        
        if endWord not in wordList:
            return 0
        
        self.visited = set()
        queue = deque([(beginWord, 0)])
        while queue:
            
            cur, counter = queue.popleft()
            counter += 1
            neighbors = list(net[cur])
            for neighbor in neighbors:
                if neighbor not in self.visited:
                    self.visited.add(neighbor)
                    queue.append((neighbor, counter))
                
            if cur == endWord:
                return counter
            
        return 0
       
#Fast String Solution
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        if endWord not in wordList:
            return 0
        current = {beginWord}
        count = 1
        alphabet = string.ascii_lowercase
        while current:
            wordList -= current
            count += 1
            nextMove = set()
            for word in current:
                for i in range(len(word)):
                    left, mid, right = word[:i], word[i], word[i+1:]
                    for char in alphabet:
                        move = left + char + right
                        if move in wordList:
                            if move == endWord:
                                return count
                            nextMove.add(move)
            current = nextMove
        return 0
                            
            
            
            
            
            
            
