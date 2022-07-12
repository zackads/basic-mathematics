from lib.points import subtract, multiply, add
from random import uniform


def line(P, A, n=999, upper=100, lower=-100):
    """
    Construct the set of points { P + tA } for n random t between upper and lower

    :param P: the start point, e.g. (1, 2)
    :param Q: another point on the line not equal to P, e.g. (4, 4)
    :param n: the order of the set of points to return.
    :param upper: the maximum t
    :return: lower: the minimum t
    """

    points = set()
    for i in range(n):
        t = uniform(lower, upper)
        tA = multiply(A, t)
        points.add(add(P, tA))

    return points
