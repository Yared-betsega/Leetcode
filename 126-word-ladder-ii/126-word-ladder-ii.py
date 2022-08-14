class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        def getShortestPath():
            queue = deque([beginWord])
            level = 0
            while queue:
                nex = set()
                parent[level] = defaultdict(set)
                for cur in queue:
                    if cur == endWord:
                        return level
                    for word in transformation[cur]:
                        nex.add(word)
                        parent[level][word].add(cur)
                    
                queue = nex     
                level += 1
            return level
        
        words = set(wordList)
        if endWord not in words:
            return []
        
        words.add(beginWord)
        n = len(beginWord)
        transformation = defaultdict(set)
        for word in words:
            for i in range(n):
                for j in range(26):
                    string = word[:i] + chr(ord("a") + j) +  word[i+1:]
                    if string in words and string  != word:
                        transformation[word].add(string)
                        
        def dfs(cur):
            if cur[-1] == beginWord:
                sh_tr_seqs.append(cur[::-1])
                return
            for word in parent[shortest - len(cur)][cur[-1]]:
                if word not in path:
                    dfs(cur + [word])
        
        parent = {}
        shortest = getShortestPath()
        visited = set([beginWord])
        sh_tr_seqs = [] # shortest transformation sequences
        dfs([endWord])
        
        return sh_tr_seqs
        
                
          