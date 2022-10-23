class Solution:
    def makeSimilar(self, nums: List[int], target: List[int]) -> int:
        evenNums = []
        evenTargets = []
        oddNums = []
        oddTargets = []
        for num, tar in zip(nums, target):
            evenNums.append(num) if not num & 1 else oddNums.append(num)
            evenTargets.append(tar) if not tar & 1 else oddTargets.append(tar)
            
        heapify(evenNums)
        heapify(evenTargets)
        answer = 0
        while evenNums:
            first, second = heappop(evenNums), heappop(evenTargets)
            if first > second:
                answer += first - second
        
        heapify(oddNums)
        heapify(oddTargets)
        while oddNums:
            first, second = heappop(oddNums), heappop(oddTargets)
            if first > second:
                answer += first - second
        
        return answer // 2

# time and space complexity
# time: O(nlog(n))
# space: O(n)