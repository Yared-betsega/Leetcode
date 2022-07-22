class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos, neg = [], []
        for num in nums:
            if num >= 0:
                pos.append(num)
            else:
                neg.append(num)
        answer = []
        left = right = 0
        for i in range(len(neg)+len(pos)):
            if i % 2 == 0:
                if right < len(pos):
                    answer.append(pos[right])
                    right += 1
                else:
                    answer.append(neg[left])
                    left += 1
            else:
                if left < len(neg):
                    answer.append(neg[left])
                    left += 1
                else:
                    answer.append(pos[right])
                    right += 1
        return answer

# time and space complexity
# time: O(n)
# space: O(n)
                    