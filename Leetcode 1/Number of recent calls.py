class RecentCounter4:

    def __init__(self):
        self.data = deque()
        self.k = 3000

    def ping(self, t: int) -> int:
        self.data.append(t)
        
        return len(self.data) - bisect_left(self.data, t - self.k)
