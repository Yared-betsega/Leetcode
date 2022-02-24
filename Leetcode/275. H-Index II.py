class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left, right = 0, len(citations)
        while left < right:
            mid = (left + right) // 2
            if citations[mid] < len(citations) - mid: 
                # print("he", left)
                left = mid + 1
            else: 
                right = mid

        return len(citations) - left
