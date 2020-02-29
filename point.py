class Point:
    def __init__(self, x, y):
        """
        Initialize Point
        x: float
        y: float
        """
        self.x = x
        self.y = y

    def dist(self, point2):
        """
        Point,Point -> float
        Returns distance between two points
        """
        return ((self.x - point2.x) ** 2 + (self.y - point2.y) ** 2) ** 0.5
