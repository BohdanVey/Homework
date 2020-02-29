import point


class Triangle:
    def __init__(self, A, B, C):
        """
        Initialize triangle
        """
        self.A = A
        self.B = B
        self.C = C

    def is_triangle(self):
        """
        Check if three points can be triangle
        Returns True, if can,
        else False
        """

        dist1 = self.A.dist(self.B)
        dist2 = self.A.dist(self.C)
        dist3 = self.C.dist(self.B)
        if dist1 + dist2 <= dist3:
            return False
        if dist3 + dist2 <= dist1:
            return False
        if dist1 + dist3 <= dist2:
            return False
        return True

    def perimeter(self):
        """
        Triangle -> float
        Returns perimeter of triangle
        """
        dist1 = self.A.dist(self.B)
        dist2 = self.A.dist(self.C)
        dist3 = self.C.dist(self.B)
        return dist1 + dist2 + dist3

    def area(self):
        """
        Triangle -> float
        Returns area of triangle
        """
        dist1 = self.A.dist(self.B)
        dist2 = self.A.dist(self.C)
        dist3 = self.C.dist(self.B)
        half_perimeter = self.perimeter() / 2
        return (half_perimeter * (half_perimeter - dist1) *
                (half_perimeter - dist2) * (half_perimeter - dist3)) ** 0.5


if __name__ == '__main__':
    tr = Triangle(point.Point(1, 1), point.Point(2, 2), point.Point(3, 3))
    print(tr.is_triangle())
    tr = Triangle(point.Point(1, 1), point.Point(3, 1), point.Point(2, 3))
    print(tr.perimeter())
    print(tr.area())
