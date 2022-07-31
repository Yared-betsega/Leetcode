
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.seg_tree = [0] * (2 * (int)(2**((int)(ceil(log2(len(self.nums)))))) -1)
        self.buildSegmentTree(0, len(nums) - 1, 0)

    def update(self, index: int, val: int) -> None:
        diff = val - self.nums[index]
        self.nums[index] = val
        self.updateSegmentTree(0, len(self.nums) - 1, index, diff, 0)

    def sumRange(self, left: int, right: int) -> int:
        return self.getSum(left, right, 0, len(self.nums) - 1, 0)
    
    
    def buildSegmentTree(self, start, end, seg_idx):
        if start == end:
            self.seg_tree[seg_idx] = self.nums[start]
            return self.nums[start]
        
        mid = (start + end) // 2
        left_segment_tree = self.buildSegmentTree(start, mid, seg_idx * 2 + 1)
        right_segment_tree = self.buildSegmentTree(mid + 1, end, seg_idx * 2 + 2)
        self.seg_tree[seg_idx] = left_segment_tree + right_segment_tree 
        return self.seg_tree[seg_idx]
    
    def updateSegmentTree(self, start, end, i, diff, seg_idx):
        if i < start or i > end:
            return;
        
        self.seg_tree[seg_idx] += diff
        if end != start:
            mid = (start + end) // 2
            self.updateSegmentTree(start, mid, i, diff, 2 * seg_idx + 1)
            self.updateSegmentTree(mid + 1, end, i, diff, 2 * seg_idx + 2)
    def getSum(self, start, end, seg_start, seg_end, seg_idx):
        if start <= seg_start and end >= seg_end:
            return self.seg_tree[seg_idx]
        
        if seg_end < start or seg_start > end:
            return 0
        
        mid = (seg_start + seg_end) // 2
        return self.getSum(start, end, seg_start, mid, 2 * seg_idx + 1 ) + self.getSum(start, end, mid + 1, seg_end, 2 * seg_idx + 2 )
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)