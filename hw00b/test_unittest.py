import unittest
import hw00b.triangle_test as triangle_test


class TestTriangleClassification(unittest.TestCase):
    def test_equilateral(self):
        self.assertEqual(triangle_test.classify_triangle(5, 5, 5), "equilateral")
    def test_isoc(self):
        self.assertEqual(triangle_test.classify_triangle(2,2,3), "isosceles")
        self.assertEqual(triangle_test.classify_triangle(4, 4, 6), "isosceles")
    def test_scalene(self):
        self.assertEqual(triangle_test.classify_triangle(7, 8, 9), "scalene")
        self.assertEqual(triangle_test.classify_triangle(3, 4, 6), "scalene")
    def test_right_triangle(self):
        self.assertEqual(triangle_test.classify_triangle(3, 4, 5), "scalene right triangle")
        self.assertEqual(triangle_test.classify_triangle(5, 12, 13), "scalene right triangle")
        self.assertEqual(triangle_test.classify_triangle(8, 15, 17), "scalene right triangle")
        self.assertEqual(triangle_test.classify_triangle(7, 24, 25), "scalene right triangle")
    def test_isosceles_right_triangle(self):
        #test case that fails becuase code does not handle floating decimals correctly
        self.assertEqual(triangle_test.classify_triangle(1, 1, 2**0.5), "isosceles right triangle")
    def test_invalid_triangles(self):
        # Edge case where 3 side lengths are not a valid trianglethat my code does not cover
        self.assertEqual(triangle_test.classify_triangle(1, 2, 3), "Not a valid triangle")
if __name__ == '__main__':
    unittest.main()
