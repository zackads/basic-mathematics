import math


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


def reflect(point, Q=(0,0)):
    """
    R_Q(P) = -(P - Q) + Q = 2Q - P

    1.  P - Q : Translate such that Q is at the origin
    2.  -(P - Q) : Reflect P with respect to the origin (P - Q)
    3.  -(P - Q) + Q : Translate back such that Q is at its original position
    """
    return subtract(dilate(Q, 2), point)