class MyCalendar:

    def __init__(self):
        self.calendar = []

    def book(self, start: int, end: int) -> bool:
        for interval in self.calendar:
            if start <= interval[0] and  end >  interval[0]:
                return False
            elif start >= interval[0] and start < interval[1]:
                return False
        self.calendar.append((start, end))
        return True
            
                


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)