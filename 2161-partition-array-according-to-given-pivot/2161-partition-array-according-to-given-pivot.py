class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        if not nums:
            return nums
        # lessThan, moreThan, equals = [], [], []
        # for num in nums:
        #     if num < pivot:
        #         lessThan.append(num)
        #     elif num == pivot:
        #         equals.append(num)
        #     else:
        #         moreThan.append(num)
        # lessThan.extend(equals)
        # lessThan.extend(moreThan)
        # return lessThan 
        
        equals = math.inf
        for i in range(len(nums)):
            if nums[i] > pivot:
                nums.append(nums[i])
                nums[i] = "0"
            elif nums[i] < pivot:
                if equals < i:
                    nums[equals], nums[i] = nums[i], nums[equals]
                    while nums[equals] != pivot:
                        equals += 1
            else:
                if equals == math.inf:
                    equals = i
                
        return list(filter(lambda x: x != "0", nums))
# time and space complexity
# time: O(n)
# space: O(n)