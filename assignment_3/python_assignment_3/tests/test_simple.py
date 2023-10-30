import unittest
import time
import collections
from gradescope_utils.autograder_utils.decorators import weight, number, visibility

from assignment3 import runErrands
from assignment3 import clipboard

runTime = 0.0

class TestDiff(unittest.TestCase):
    global runTime
    start_time = time.time()

    @weight(10)
    def test_1(self):
        """runErrands - Test Case 1"""
        graph1 = [['b','c','d'],['a'],['a'],['a']]
        val = runErrands(graph1)
        self.assertEqual(val, 4)

    @weight(10)
    def test_2(self):
        """runErrands - Test Case 2"""
        graph2 = [['b'],['a', 'c'],['b'],['a']]
        val = runErrands(graph2)
        self.assertEqual(val, 3)
        

    @weight(10)
    def test_3(self):
        """runErrands - Test Case 3"""
        graph3 = [['b','c'],['a', 'b'],['a', 'd'],['c'],['b']]
        val = runErrands(graph3)
        self.assertEqual(val, 4)

    @weight(10)
    def test_4(self):
        """runErrands - Test Case 4"""
        graph4 = [['b', 'c'],['a', 'c'],['a', 'b', 'd', 'e'],['c', 'e'], ['c', 'd'], ['e']]
        val = runErrands(graph4)
        self.assertEqual(val, 5)
    
    @weight(10)
    def test_5(self):
        """runErrands - Test Case 5"""
        graph5 = [['b'],['a','d', 'e'],['d'],['b', 'e'],['b','d']]
        val = runErrands(graph5)
        self.assertEqual(val, 4)

    @weight(10)
    def test_6(self):
        """clipboard - Test Case 1"""
        clip = clipboard(2)
        clip.copy(1, 1)
        result1 = clip.paste(1); # Expected: 1
        self.assertEqual(result1, 1)

    @weight(10)
    def test_7(self):
        """clipboard - Test Case 2"""
        # case 2: ints only
        clip = clipboard(5)

        clip.copy(1, 1)  # Clipboard is {1=1}
        clip.copy(2, 2)  # Clipboard is {1=1, 2=2}
        clip.copy(3, 3)  # Clipboard is {1=1, 2=2, 3=3}
        clip.copy(4, 4)  # Clipboard is {1=1, 2=2, 3=3, 4=4}
        clip.copy(5, 5)  # Clipboard is {1=1, 2=2, 3=3, 4=4, 5=5}
        result2a = clip.paste(1) #Expected: 1
        result2b = clip.paste(2) #Expected: 2
        result2c = clip.paste(3) #Expected: 3
        result2d = clip.paste(4) #Expected: 4
        clip.copy(6, 6)  # Clipboard is {1=1, 2=2, 3=3, 4=4, 5=5} // evict 5
        
        result2e = clip.paste(5); # should be -1

        self.assertEqual((result2a, result2b, result2c, result2d, result2e), (1, 2, 3, 4, -1))


    @weight(10)
    def test_8(self):
        """clipboard - Test Case 3"""
        clip = clipboard(2)

        clip.copy(1, 1) #  // Clipboard is {1=1}
        result3a = clip.paste(1) # // Expected: 1
        clip.copy(2, 2) # // Clipboard is {1=1, 2=2}
        clip.copy(3, 3) # // Clipboard is {1=1, 3=3} evict 2
        result3b = clip.paste(2) # // Expected: -1
        result3c = clip.paste(3) # // Expected: 3
        
        self.assertEqual((result3a, result3b, result3c), (1, -1, 3))

    @weight(10)
    def test_9(self):
        """clipboard - Test Case 4"""
        clip = clipboard(1)

        clip.copy(1, 1)  # // Clipboard is {1=1}
        result4a = clip.paste(1); # // Expected: 1
        clip.copy(2, 2)  # // Clipboard is {2=2}
        result4b = clip.paste(2) # // Expected: 2
        result4c = clip.paste(1) # // Expected: -1

        self.assertEqual((result4a, result4b, result4c), (1, 2, -1))

    @weight(10)
    def test_10(self):
        """clipboard - Test Case 5"""
        clip = clipboard(1)
        result5a = clip.paste(1); # Expected: -1
        result5b = clip.paste(2); # Expected: -1
        self.assertEqual((result5a, result5b), (-1,-1))        

    runTime = time.time() - start_time
