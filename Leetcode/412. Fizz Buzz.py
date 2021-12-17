class Solution:
    def fizzBuzz(self, n):
        answer = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                answer.append("FizzBuzz")
                continue
            elif i % 3 == 0:
                answer.append("Fizz")
                continue
            elif i % 5 == 0:
                answer.append("Buzz")
                continue
            else:
                answer.append(str(i))
        return answer
a = Solution()
print(a.fizzBuzz(15))
            
