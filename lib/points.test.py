import unittest

from lib.points import subtract, multiply, add, dilate


class PointsTests(unittest.TestCase):
    def test_addition_in_two_dimensions(self):
        P = (1, 2)
        Q = (3, 4)

        sum = add(P, Q)

        self.assertEqual(sum, (4, 6))

    def test_subtraction_in_two_dimensions(self):
        P = (1, 2)
        Q = (3, 4)

        difference = subtract(P, Q)

        self.assertEqual(difference, (-2, -2))

    def test_subtraction_in_three_dimensions(self):
        P = (1, 2, 3)
        Q = (4, 5, 6)

        difference = subtract(P, Q)

        self.assertEqual(difference, (-3, -3, -3))

    def test_multiplication_in_two_dimensions(self):
        P = (1, 2)
        s = 2

        product = multiply(P, s)

        self.assertEqual(product, (2, 4))

    def test_multiplication_in_three_dimensions(self):
        P = (1, 2, 3)
        s = 2

        product = multiply(P, s)

        self.assertEqual(product, (2, 4, 6))

    def test_dilation_in_two_dimensions_wrt_the_origin(self):
        P = (1, 2)
        r = 2

        dilation = dilate(P, r)

        self.assertEqual(dilation, (2, 4))

    def test_dilation_in_three_dimensions_wrt_the_origin(self):
        P = (2, 5, 7)
        r = 3

        dilation = dilate(P, r)

        self.assertEqual(dilation, (6, 15, 21))



if __name__ == '__main__':
    unittest.main()

#%%
