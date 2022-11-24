class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        @lru_cache(None)
        def dp(i, maxHeight, width):
            if i >= len(books):
                return maxHeight
            
            if books[i][0] > width:
                return maxHeight + dp(i + 1, books[i][1], shelfWidth - books[i][0])
            
            put = dp(i + 1, max(maxHeight, books[i][1]), width - books[i][0])
            dontPut = maxHeight + dp(i + 1, books[i][1], shelfWidth - books[i][0])
            return min(put, dontPut)
        
        return dp(0, 0, shelfWidth)
    
            
            
            