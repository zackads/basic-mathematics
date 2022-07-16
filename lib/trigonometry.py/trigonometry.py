def pi():
    """
    The ratio of the circumference of a circle to its diameter, approximated using Leibniz' formula

    See https://en.wikipedia.org/wiki/Leibniz_formula_for_%CF%80

    :return: an approximation of pi accurate to six decimal places
    """
    additions = 0
    subtractions = 0
    flag = True
    for k in range(3, 10000006, 2):
        if flag:  # 3, 7, 11, ...
            subtractions += 1 / k
            flag = False
        else:  # 5, 9, 13, ...
            additions += 1 / k
            flag = True

    return 4 * (1 - subtractions + additions)

def rad(deg):
    """
    Given the measure of an angle in degrees, approximate the equivalent in radians

    :param deg: the measure of an angle in degrees
    :return: an approximate measure of the same angle in radians
    """
    return (deg / 360) * (2 * pi())

def deg(rad):
    """
    Given the measure of an angle in radians, calculate the equivalent in radians

    :param rad:
    :return:
    """
    return (rad / 2 * pi()) * 360