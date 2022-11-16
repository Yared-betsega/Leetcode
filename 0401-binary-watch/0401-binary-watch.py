class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        def count(time):
            n = 0
            for i in range(32):
                if time & (1 << i):
                    n += 1
            return n
        
        answer = []
        for hour in range(12):
            for minute in range(60):
                if count(hour) + count(minute) == turnedOn:
                    answer.append(str(hour) + ":" + f'{minute:02}')
        
        return answer
        
        
            