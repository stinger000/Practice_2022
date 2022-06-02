class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"Точка с координатами x={self.x}, y={self.y}"

    def distance_to(self, other) -> float:
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5


def print_point(p: Point):
    print(f"({p.x}, {p.y})")


def get_point_from_keyboard() -> Point:
    x, y = [float(i) for i in input("Введете координаты точки через пробел: ").split()]
    return Point(x, y)


p = get_point_from_keyboard()
q = get_point_from_keyboard()

# print_point(p)
print(p)
print(q)
print(f"Расстояние равно {p.distance_to(q)}")