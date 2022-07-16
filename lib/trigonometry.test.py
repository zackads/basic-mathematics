import unittest

from lib.trigonometry import pi_approx, rad, deg


class TrigonometryTests(unittest.TestCase):
    def test_pi(self):
        self.assertAlmostEqual(pi_approx(), 3.14159265)

    def test_rad(self):
        pi = 3.14159265
        self.assertAlmostEqual(rad(15), pi / 12)
        self.assertAlmostEqual(rad(75), (5 * pi) / 12)
        self.assertAlmostEqual(rad(105), 7 * pi / 12)
        self.assertAlmostEqual(rad(120), 2 / 3 * pi)
        self.assertAlmostEqual(rad(135), 3 / 4 * pi)
        self.assertAlmostEqual(rad(150), 5 / 6 * pi)
        self.assertAlmostEqual(rad(165), 11 / 12 * pi)
        self.assertAlmostEqual(rad(20), pi / 9)
        self.assertAlmostEqual(rad(40), 2 * pi / 9)
        self.assertAlmostEqual(rad(140), 7 * pi / 9)
        self.assertAlmostEqual(rad(310), 31 * pi / 18)

    def test_deg(self):
        pi = 3.14159265
        self.assertAlmostEqual(deg(pi / 4), 45)
        self.assertAlmostEqual(deg(- pi / 4), -45)
        self.assertAlmostEqual(deg(8 * pi / 9), 160)
        self.assertAlmostEqual(deg(5 * pi / 9), 100)
        self.assertAlmostEqual(deg(7 * pi / 4), 315)
        self.assertAlmostEqual(deg(14 * pi / 3), 840)
        self.assertAlmostEqual(deg(22 * pi / 3), 1320)
        self.assertAlmostEqual(deg(- pi / 3), -60)


if __name__ == '__main__':
    unittest.main()
