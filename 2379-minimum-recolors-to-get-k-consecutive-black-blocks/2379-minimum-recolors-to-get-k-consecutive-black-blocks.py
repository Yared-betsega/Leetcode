class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left, right = 0, k-1
        res = float("inf")
        while right < len(blocks):
            res = min(res, blocks[left: right + 1].count("W"))
            left += 1
            right += 1
        return res