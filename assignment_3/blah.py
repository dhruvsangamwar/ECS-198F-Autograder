import unittest

class TestDiff(unittest.TestCase):
    def test1(self):
        a = 1 
        b = 2
        c = 3
        self.assertEqual((a, b, c), (1, 2, 5))


if __name__ == "__main__":
    TestDiff.test1
