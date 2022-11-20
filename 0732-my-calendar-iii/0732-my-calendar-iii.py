class MyCalendarThree:

    def __init__(self):
        self.calendar = []

    def book(self, start: int, end: int) -> int:
        bisect.insort(self.calendar, (start, 1))
        bisect.insort(self.calendar, (end, -1))
        
        prevBookings = 0
        answer = 0
        for t, sign in self.calendar:
            prevBookings += sign
            answer = max(answer, prevBookings)
        return answer
# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)