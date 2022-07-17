import math
from random import uniform


def distance(P, Q):
    differences = [q - p for p, q in zip(P, Q)]
    squared = [d ** 2 for d in differences]
    return math.sqrt(squared)

    return math.sqrt(((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2))


def subtract(P, Q):
    """P - Q for some points P and Q"""
    return tuple(p - q for p, q in zip(P, Q))


def add(P, Q):
    return tuple(p + q for p, q in zip(P, Q))


def multiply(P, s):
    """rP for some point P and scalar multiplier r"""
    return tuple(s * p for p in P)


def dilate(P, r, Q=(0, 0, 0)):
    """
    Dilate P by r with respect to some point Q.

    By default P = (0, 0, 0), i.e. the origin.
    """
    return add(multiply(subtract(P, Q), r), Q)


def reflect(point, Q=(0, 0)):
    """
    R_Q(P) = -(P - Q) + Q = 2Q - P

    1.  P - Q : Translate such that Q is at the origin
    2.  -(P - Q) : Reflect P with respect to the origin (P - Q)
    3.  -(P - Q) + Q : Translate back such that Q is at its original position
    """
    return subtract(dilate(Q, 2), point)


def points(f, interval=[-100, 100]):
    """Returns the set of points (x, f(x)) in the interval"""
    p = []
    xs = float_range(*interval, 0.1)

    for x in xs:
        p.append((x, f(x)))

    return p

def float_range(start: int, stop: int, step:float=0.1):
    steps = int((stop - start) / step)
    r = [start]

    for i in range(steps - 1):
        r.append(round(r[i] + step, 2))

    return r