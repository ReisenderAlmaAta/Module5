class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def piece(self, other):
        x1 = self.x
        y1 = self.y
        x2 = other.x
        y2 = other.y
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


p1 = Point(int(input('Координаты точки 1 по оси X: ')), int(input('Координаты точки 1 по оси Y: ')))
p2 = Point(int(input('Координаты точки 2 по оси X: ')), int(input('Координаты точки 2 по оси Y: ')))

print(Point.piece(p1, p2))