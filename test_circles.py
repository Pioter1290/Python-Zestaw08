import math
import unittest
from points import Point
from circles import Circle


class TestCircle(unittest.TestCase):

    def test__init__(self):
        circle = Circle(0, 0, 5)
        self.assertEqual(circle.pt.x, 0)
        self.assertEqual(circle.pt.y, 0)
        self.assertEqual(circle.radius, 5)

    def test__init__invalid_radius(self):
        with self.assertRaises(ValueError):
            Circle(0, 0, -5)

    def test__repr__(self):
        circle = Circle(1, 2, 3)
        self.assertEqual(repr(circle), "Circle(1, 2, 3)")

    def test__eq__(self):
        circle1 = Circle(0, 0, 5)
        circle2 = Circle(0, 0, 5)
        circle3 = Circle(1, 1, 5)
        self.assertTrue(circle1 == circle2)
        self.assertFalse(circle1 == circle3)

    def test__ne__(self):
        circle1 = Circle(0, 0, 5)
        circle2 = Circle(0, 0, 5)
        circle3 = Circle(1, 1, 5)
        self.assertFalse(circle1 != circle2)
        self.assertTrue(circle1 != circle3)

    def test_area(self):
        circle = Circle(0, 0, 5)
        expected_area = math.pi * 5 ** 2
        self.assertEqual(circle.area(), expected_area)

    def test_move(self):
        circle = Circle(0, 0, 5)
        moved_circle = circle.move(2, 3)
        self.assertEqual(moved_circle.pt.x, 2)
        self.assertEqual(moved_circle.pt.y, 3)
        self.assertEqual(moved_circle.radius, 5)

        circle2 = Circle(1, 6, 7)
        moved_circle2 = circle2.move(6, 4)
        self.assertEqual(moved_circle2.pt.x, 7)
        self.assertEqual(moved_circle2.pt.y, 10)
        self.assertEqual(moved_circle2.radius, 7)

    def test_cover(self):
        circle1 = Circle(0, 0, 1)
        circle2 = Circle(2, 0, 1)
        covered_circle = circle1.cover(circle2)
        self.assertEqual(covered_circle.pt.x, 1)
        self.assertEqual(covered_circle.pt.y, 0)
        self.assertEqual(covered_circle.radius, 2)

        # Gdy okręgi się nie przecinają
        circle3 = Circle(-1, 0, 1)
        circle4 = Circle(3, 0, 1)
        covered_circle2 = circle3.cover(circle4)
        self.assertEqual(covered_circle2.pt.x, 1)
        self.assertEqual(covered_circle2.pt.y, 0)
        self.assertEqual(covered_circle2.radius, 3)

        # Gdy okręgi się przecinają
        circle5 = Circle(-2, 0, 2)
        circle6 = Circle(0, 0, 1)
        covered_circle3 = circle5.cover(circle6)
        self.assertEqual(covered_circle3.pt.x, -1.5)
        self.assertEqual(covered_circle3.pt.y, 0)
        self.assertEqual(covered_circle3.radius, 2.5)

        circle7 = Circle(-2, 0, 3)
        circle8 = Circle(1, 4, 3)
        covered_circle4 = circle7.cover(circle8)
        self.assertEqual(covered_circle4.pt.x, -0.5)
        self.assertEqual(covered_circle4.pt.y, 2)
        self.assertEqual(covered_circle4.radius, 5.5)

    def test_from_points(self):
        p1 = Point(0, 0)
        p2 = Point(1, 0)
        p3 = Point(0, 1)
        circle = Circle.from_points((p1, p2, p3))
        self.assertEqual(circle.pt.x, 0.5)
        self.assertEqual(circle.pt.y, 0.5)
        self.assertEqual(circle.radius, math.sqrt(0.5))

        p4 = Point(1, 1)
        p5 = Point(-1, -1)
        p6 = Point(-1, 1)
        circle2 = Circle.from_points((p4, p5, p6))
        self.assertEqual(circle2.pt.x, 0)
        self.assertEqual(circle2.pt.y, 0)
        self.assertEqual(circle2.radius, math.sqrt(2))

        p7 = Point(0, 3)
        p8 = Point(-3, 0)
        p9 = Point(0, -3)
        circle2 = Circle.from_points((p7, p8, p9))
        self.assertEqual(circle2.pt.x, 0)
        self.assertEqual(circle2.pt.y, 0)
        self.assertEqual(circle2.radius, 3)

    def test_circle_bounding_box(self):
        circle = Circle(0, 0, 5)
        assert circle.top == 5
        assert circle.bottom == -5
        assert circle.left == -5
        assert circle.right == 5
        assert circle.width == 10
        assert circle.height == 10
        assert circle.topleft == Point(-5, 5)
        assert circle.topright == Point(5, 5)
        assert circle.bottomleft == Point(-5, -5)
        assert circle.bottomright == Point(5, -5)


if __name__ == '__main__':
    unittest.main()
