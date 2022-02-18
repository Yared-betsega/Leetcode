class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index1 = 0
        index2 = 1
        while index1 < len(numbers):
            if numbers[index1] + numbers[index2] == target:
                return [index1 + 1, index2 + 1]
            else:
                index2 += 1
            if index2 == len(numbers):
                tested = index1
                index1 += 1
                while numbers[index1] == numbers[tested]:
                    index1 += 1
                index2 = index1 + 1
