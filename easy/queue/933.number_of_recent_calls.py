class RecentCounter:

    def __init__(self):
        self.count = []

    def ping(self, t: int) -> int:
        self.count.append(t)
        while t - self.count[0] > 3000:
            self.count.pop(0)   
        return len(self.count)



# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
