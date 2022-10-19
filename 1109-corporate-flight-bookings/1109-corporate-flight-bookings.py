class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        prefixArray = [0] * (n + 1)
        for first, last, seats in bookings:
            prefixArray[first] += seats
            if last + 1 <= n:
                prefixArray[last + 1] -= seats
        answer = []
        total = 0
        for i in range(1, n + 1):
            total += prefixArray[i]
            answer.append(total)
        
        return answer