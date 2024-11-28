import math
from points import Point


class Circle:

    def __init__(self, x, y, radius):
        if radius < 0:
            raise ValueError("promień ujemny")
        self.pt = Point(x, y)
        self.radius = radius

    def __repr__(self):
        return f"Circle({self.pt.x}, {self.pt.y}, {self.radius})"

    def __eq__(self, other):
        return self.pt == other.pt and self.radius == other.radius

    def __ne__(self, other):
        return not self == other

    def area(self):  # pole powierzchni
        return math.pi * self.radius ** 2

    def move(self, x, y):  # przesuniecie o (x, y)
        return Circle(self.pt.x + x, self.pt.y + y, self.radius)

    def cover(self, other):  # najmniejszy okrąg pokrywający oba
        distance = math.sqrt((self.pt.x - other.pt.x) ** 2 + (self.pt.y - other.pt.y) ** 2)
        if distance + other.radius <= self.radius:
            return self
        if distance + self.radius <= other.radius:
            return other
        new_radius = (distance + self.radius + other.radius) / 2

        dx = other.pt.x - self.pt.x
        dy = other.pt.y - self.pt.y
        factor = (new_radius - self.radius) / distance if distance != 0 else 0
        new_x = self.pt.x + dx * factor
        new_y = self.pt.y + dy * factor
        return Circle(new_x, new_y, new_radius)

    @classmethod
    def from_points(cls, points):
        if len(points) != 3:
            raise ValueError("Wymagane są dokladnie 3 punkty")

        p1, p2, p3 = points

        x1, y1 = p1.x, p1.y
        x2, y2 = p2.x, p2.y
        x3, y3 = p3.x, p3.y

        A = x1 * (y2 - y3) - y1 * (x2 - x3) + x2 * y3 - x3 * y2
        if A == 0:
            raise ValueError("Punkty są współliniowe")

        B = (x1 ** 2 + y1 ** 2) * (y3 - y2) + (x2 ** 2 + y2 ** 2) * (y1 - y3) + (x3 ** 2 + y3 ** 2) * (y2 - y1)
        C = (x1 ** 2 + y1 ** 2) * (x2 - x3) + (x2 ** 2 + y2 ** 2) * (x3 - x1) + (x3 ** 2 + y3 ** 2) * (x1 - x2)
        D = (x1 ** 2 + y1 ** 2) * (x3 * y2 - x2 * y3) + (x2 ** 2 + y2 ** 2) * (x1 * y3 - x3 * y1) + (
                    x3 ** 2 + y3 ** 2) * (x2 * y1 - x1 * y2)

        cx = -B / (2 * A)
        cy = -C / (2 * A)
        radius = math.sqrt((B ** 2 + C ** 2 - 4 * A * D) / (4 * A ** 2))

        return cls(cx, cy, radius)

    @property
    def top(self):
        return self.pt.y + self.radius

    @property
    def bottom(self):
        return self.pt.y - self.radius

    @property
    def left(self):
        return self.pt.x - self.radius

    @property
    def right(self):
        return self.pt.x + self.radius

    @property
    def width(self):
        return 2 * self.radius

    @property
    def height(self):
        return 2 * self.radius

    @property
    def topleft(self):
        return Point(self.left, self.top)

    @property
    def bottomleft(self):
        return Point(self.left, self.bottom)

    @property
    def topright(self):
        return Point(self.right, self.top)

    @property
    def bottomright(self):
        return Point(self.right, self.bottom)
