import triangle
import point

if __name__ == '__main__':
    triangle = triangle.Triangle(point.Point(1, 1), point.Point(3, 1), point.Point(2, 3))
    assert triangle.is_triangle()
    assert triangle.perimeter() == 6.47213595499958
    assert triangle.area() == 2.0