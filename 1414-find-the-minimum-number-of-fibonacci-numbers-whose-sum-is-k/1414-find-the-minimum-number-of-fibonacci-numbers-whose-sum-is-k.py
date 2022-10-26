class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        fibs = [1]
        first, second = 1, 1
        while second <= k:
            fibs.append(second)
            first, second = second, first + second


        answer = 0
        while k > 0:
            k  -= fibs[bisect_right(fibs, k) - 1]
            answer += 1

        return answer
