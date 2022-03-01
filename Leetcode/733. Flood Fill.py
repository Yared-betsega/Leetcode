class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        self.image = image
        self.newColor = newColor
        self.visited = set()
        self.target = image[sr][sc]
        def helper(sr, sc):
            if (sr, sc) not in self.visited:
                if sr >= 0 and sr < len(self.image) and sc >= 0 and sc < len(self.image[sr]):
                    if self.image[sr][sc] == self.target:
                        self.image[sr][sc] = newColor
                        self.visited.add((sr, sc))
                        helper(sr - 1, sc)
                        helper(sr + 1, sc)
                        helper(sr, sc - 1)
                        helper(sr, sc + 1)
                        
        helper(sr, sc)  
        
        return self.image
        
