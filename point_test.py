import point

if __name__ == '__main__':
    x1, y1 = [float(x) for x in input('Print x and y coordinates: ').split()]
    x2, y2 = [float(x) for x in input('Print x and y coordinates: ').split()]
    user_point1 = point.Point(x1, y1)
    user_point2 = point.Point(x2, y2)
    print('Distance between two points:' + str(user_point1.dist(user_point2)))
