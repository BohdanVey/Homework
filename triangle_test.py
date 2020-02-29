import triangle
import point

if __name__ == '__main__':
    x, y = [float(x) for x in input('Print x and y coordinates: ').split()]
    point1 = point.Point(x, y)
    x, y = [float(x) for x in input('Print x and y coordinates: ').split()]
    point2 = point.Point(x, y)
    x, y = [float(x) for x in input('Print x and y coordinates: ').split()]
    point3 = point.Point(x, y)
    user_triangle = triangle.Triangle(point1, point2, point3)
    if not user_triangle.is_triangle():
        print('This is not triangle')
    else:
        print('This is triangle')
        print('Perimeter is: ' + str(user_triangle.perimeter()))
        print('Area is: ' + str(user_triangle.area()))
