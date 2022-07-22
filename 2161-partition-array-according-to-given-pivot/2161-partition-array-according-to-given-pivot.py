class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        if not nums:
            return nums
        lessThan, moreThan, equals = [], [], []
        for num in nums:
            if num < pivot:
                lessThan.append(num)
            elif num == pivot:
                equals.append(num)
            else:
                moreThan.append(num)
        lessThan.extend(equals)
        lessThan.extend(moreThan)
        return lessThan 
    
# time and space complexity
# time: O(n)
# space: O(1)