import math
from random import uniform


def circle(r, centre=(0, 0), n=999):
    """
    Construct a set of points at distance r from centre.  I.e. an approximate circle.

    In mathematical reality, the set is infinite.

    :param r: radius, e.g. 3
    :param centre: point, e.g. (1, 2).  Defaults to (0, 0)
    :param n: the order of the set of points to return.
    :return: a set of random points on the circle's circumference
    """

    points = set()
    for i in range(n):
        x = uniform(centre[0] - r, centre[0] + r)
        y_pos = math.sqrt(r ** 2 - (x - centre[0]) ** 2) + centre[1]
        y_neg = centre[1] - (y_pos - centre[1])
        points.add((x, y_pos))
        points.add((x, y_neg))

    return points
