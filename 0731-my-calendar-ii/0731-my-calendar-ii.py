class MyCalendarTwo:

    def __init__(self):
        self.calendar = []
        self.doubles = []

    def book(self, start: int, end: int) -> bool:
        for interval in self.doubles:
            if start <= interval[0] and  end >  interval[0]:
                return False
            elif start >= interval[0] and start < interval[1]:
                return False
                
        for interval in self.calendar:
            if start <= interval[0] and  end >  interval[0]:
                self.doubles.append([max(start, interval[0]), min(end, interval[1])])

            elif start >= interval[0] and start < interval[1]:
                self.doubles.append([max(start, interval[0]), min(end, interval[1])])
                    
        self.calendar.append([start, end]) 
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)