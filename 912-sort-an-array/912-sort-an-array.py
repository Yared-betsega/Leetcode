class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(array):
            if len(array) == 1:
                return array
            
            mid = len(array) // 2
            left = mergeSort(array[:mid])
            right = mergeSort(array[mid:])
            l =  r = 0
            temp = []
            for i in range(len(array)):
                if l == len(left):
                    temp += right[r:]
                    break
                elif r == len(right):
                    temp += left[l:]
                    break
                else:
                    if left[l] <= right[r]:
                        temp.append(left[l])
                        l += 1
                    else:
                        temp.append(right[r])
                        r += 1
            return temp
        
        return mergeSort(nums)

# time and space complexity
# time: O(nlogn)
# space: O(n)
                                
                    