class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)
        answer = set()
        for num in nums:
            count[num] += 1
            if count[num] > len(nums) / 3:
                answer.add(num)
        return answer