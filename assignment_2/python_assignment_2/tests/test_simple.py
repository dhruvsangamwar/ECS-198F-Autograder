import unittest
import time
import collections
from gradescope_utils.autograder_utils.decorators import weight, number, visibility
from assignment2 import findCycle
from linkedList import LinkedList

runTime = 0.0

class TestDiff(unittest.TestCase):
    global runTime
    start_time = time.time()

    @weight(20)
    def test_1(self):
        """Test Case 1"""
        arr1 = ["red_left", "blue_left", "blue_right", "red_right"]
        val = findCycle(arr1)
        self.assertEqual(val, 'True')

    @weight(20)
    def test_2(self):
        """Test Case 2"""
        arr2 = ["red_left", "blue_right"]
        val = isValidBracelet(arr2)
        self.assertEqual(val, 'False')

    @weight(20)
    def test_3(self):
        """Test Case 3"""
        arr3 = ["red_left", "red_right", "blue_left", "blue_right"]
        val = isValidBracelet(arr3)
        self.assertEqual(val, 'True')

    @weight(20)
    def test_4(self):
        """Test Case 4"""
        arr4 = []
        val = isValidBracelet(arr4)
        self.assertEqual(val, 'True')
    
    @weight(20)
    def test_5(self):
        """Test Case 5"""
        arr5 = ["red_left", "blue_left", "yellow_left", "yellow_right", "blue_right", "red_right"]
        val = isValidBracelet(arr5)
        self.assertEqual(val, 'True')

    runTime = time.time() - start_time
