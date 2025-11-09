class ponit:
    def __init__(self , x, y):
        self.y = y
    def getpoint(self):
        return f"point({self.x},  {self.y})"
    p1 = point(4, 7)
    print(p1.getpoint())