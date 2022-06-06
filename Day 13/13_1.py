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


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_exist(self):
        return self.a + self.b > self.c and \
               self.a + self.c > self.b and \
               self.b + self.c > self.a

    def area(self):
        if not self.is_exist():
            return -1
        p = (self.a + self.b + self.c) / 2
        s = (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5
        return s

    def is_rectangle(self):
        return self.a == self.b or self.a == self.c or self.b == self.c

    def is_equilateral(self):
        return self.a == self.b and self.b == self.c

class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b

    def is_rectangle(self):
        return True

    def is_equilateral(self):
        return False

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius ** 2 * math.pi

class Ellipse:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b * math.pi

    def is_rectangle(self):
        return False


class Hypercube:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        return self.a * self.b * self.c

    def is_rectangle(self):
        return False

    def is_equilateral(self):
        return False


def make_triangle_from_points(p1: Point, p2: Point, p3: Point) -> Triangle:
    a = p1.distance_to(p2)
    b = p2.distance_to(p3)
    c = p3.distance_to(p1)
    return Triangle(a, b, c)


def make_triangle_from_keyboard() -> Triangle:
    """
    Запрашивает у пользователя ввод координат,
    и составляет треугольник с вершинами во
    введенных координатах.
    """
    t = make_triangle_from_points(
        get_point_from_keyboard(),
        get_point_from_keyboard(),
        get_point_from_keyboard()
    )
    return t


def test_1():
    triangles = []
    for i in range(2):
        triangles.append(make_triangle_from_keyboard())

    for t in triangles:
        area = t.area()
        if area > 0:
            print(area)
        else:
            print("Такого треугольника нет")




if __name__ == '__main__':
    test_1()
