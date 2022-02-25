class Solution:
    def shipWithinDays(self, weights, days):
        left = max(weights)
        right = sum(weights)
        answer = right
        while left <= right:
            mid = (left + right) // 2
            possible = self.isPossible(weights, mid, days)
            if possible:
                answer = mid
                right = mid - 1
            else:
                left = mid + 1
        return answer
    def isPossible(self, weights, capacity, days):
        counter = total = 0
        for right in range(len(weights)):
            total += weights[right]
            
            if weights[right] > capacity:
                return False
            if total > capacity:
                counter += 1
                total = weights[right]
        if total > 0:
            counter += 1
        return True if counter <= days else False
    
# time and space complexity
# time complexity = O(nlog(n)), n == len(weights)
# space complexity = O(1)
