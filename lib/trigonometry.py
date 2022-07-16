def pi_approx():
    """
    The ratio of the circumference of a circle to its diameter,
    approximated using the Bailey–Borwein–Plouffe formula

    See https://en.wikipedia.org/wiki/Bailey%E2%80%93Borwein%E2%80%93Plouffe_formula

    :return: an approximation of pi accurate to 7 decimal places
    """

    def bailey_borwein_plouffe(k):
        return (1 / 16 ** k) * (4 / (8 * k + 1) - 2 / (8 * k + 4) - 1 / (8 * k + 5) - 1 / (8 * k + 6))

    return series(bailey_borwein_plouffe, 0, 100)


def series(f, k=0, n=10):
    """
    Calculate the value of the series defined by f between k and n

    :param f: the function that defines the terms
    :param k: the lower limit
    :param n: the upper limit
    :return:
    """
    return sum([f(k) for k in range(k, n)])


def rad(deg):
    """
    Given the measure of an angle in degrees, approximate the equivalent in radians

    :param deg: the measure of an angle in degrees
    :return: an approximate measure of the same angle in radians
    """
    return (deg / 360) * (2 * pi_approx())


def deg(rad):
    """
    Given the measure of an angle in radians, calculate the equivalent in radians

    :param rad:
    :return:
    """
    return round((rad / (2 * pi_approx())) * 360, 2)


def sine(rad, pairs=100):
    """
    Approximate the sine of an angle measured in radians using the Taylor series of the sine function

    https://en.wikipedia.org/wiki/Taylor_series

    :param rad: the measure of an angle in radians
    :param pairs: the number of pairs of additions and subtractions to make in the Taylor series approximation
    :return: an approximate value of the sine function at rad
    """
    result = rad
    flag = True
    for k in range(3, pairs + 2, 2):
        if flag:  # 3, 3, 7, 11, ...
            result -= rad ** k / factorial(k)
            flag = False
        else:  # 5, 9, 13, ...
            result += rad ** k / factorial(k)
            flag = True

    return result


def cosine(rad, pairs=100):
    """
    Approximate the cosine of an angle measured in radians using the Taylor series of the sine function

    :param rad: the measure of an angle in radians
    :param pairs: the number of pairs of additions and subtractions to make in the Taylor series approximation
    :return: an approximate value of the cosine function at rad
    """
    return sine(rad + pi_approx() / 2, pairs)


def factorial(n):
    if n < 0:
        raise ValueError("n must be greater than 0")

    k = n - 1
    while k >= 1:
        n = n * k
        k = k - 1
    return n
