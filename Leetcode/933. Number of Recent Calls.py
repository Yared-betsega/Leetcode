class RecentCounter:

    def __init__(self):
        self.lst = []

    def ping(self, t: int) -> int:
        self.lst.append(t)
        while True:
            if self.lst[0]<t-3000:
                self.lst.pop(0)
            else:
                return len(self.lst)
