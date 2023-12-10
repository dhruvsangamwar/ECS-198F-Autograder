import time
import unittest
from gradescope_utils.autograder_utils.decorators import weight
import subprocess

runTime = 0.0

class TestDiff(unittest.TestCase):
    def setUp(self):
        pass 

    global runTime
    start_time = time.time()

    # Associated point value within GradeScope
    @weight(0)
    def test_Compile(self):
        #Title used by Gradescope 
        """Clean Compile"""

        # Create a subprocess to run our make file to ensure it compiles 
        test = subprocess.Popen(["make"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stderr.read().strip().decode('utf-8')
        test.kill()

        # Standard unit test case with an associated error message 
        self.assertTrue( output == "", msg=output)
        test.terminate()

    # Associated point value within GradeScope
    @weight(0.1)
    def test_case1(self):
        #Title used by Gradescope 
        """Test Case 1: Tests predict_tree_height()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "0"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "102.305"
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()
    
    # Associated point value within GradeScope
    @weight(0.1)
    def test_case2(self):
        #Title used by Gradescope 
        """Test Case 2: Tests predict_tree_height()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "1"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "99.87"
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()

    # Associated point value within GradeScope
    @weight(0.1)
    def test_case3(self):
       #Title used by Gradescope 
        """Test Case 3: Tests predict_tree_height()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "2"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "97.22"
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()
    
    @weight(0.1)
    def test_case4(self):
       #Title used by Gradescope 
        """Test Case 4: Tests predict_tree_height()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "3"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "-1"
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()
    
    @weight(0.1)
    def test_case5(self):
       #Title used by Gradescope 
        """Test Case 5: Tests predict_tree_height()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "4"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "101.9575"
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()
    
    @weight(0.1)
    def test_case6(self):
       #Title used by Gradescope 
        """Test Case 6: Tests predict_tree_height()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "5"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "102.278"
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()
    
    @weight(0.1)
    def test_case7(self):
       #Title used by Gradescope 
        """Test Case 7: Tests predict_tree_height()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "6"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "-1"
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()

    @weight(0.1)
    def test_case8(self):
       #Title used by Gradescope 
        """Test Case 8: Tests predict_tree_height()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "7"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "78.9"
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()
    
    @weight(0.1)
    def test_case9(self):
       #Title used by Gradescope 
        """Test Case 9: Tests predict_tree_height()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "8"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "83.55"
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()
    
    @weight(0.1)
    def test_case10(self):
       #Title used by Gradescope 
        """Test Case 10: Tests predict_tree_height()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "9"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "77.5"
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()
    
    @weight(0.1)
    def test_case11(self):
       #Title used by Gradescope 
        """Test Case 11: Tests predict_tree_height()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "10"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "82.625"
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()
    
    @weight(0.1)
    def test_case12(self):
       #Title used by Gradescope 
        """Test Case 12: Tests predict_tree_height()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "11"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "88.3"
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()
    
    @weight(0.1)
    def test_case13(self):
       #Title used by Gradescope 
        """Test Case 13: Tests predict_tree_height()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "12"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "82.75"
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()
    
    @weight(0.1)
    def test_case14(self):
       #Title used by Gradescope 
        """Test Case 14: Tests predict_tree_height()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "13"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "-1"
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()
    
    @weight(0.1)
    def test_case15(self):
       #Title used by Gradescope 
        """Test Case 15: Tests predict_tree_height()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "14"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "30"
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()
    
    @weight(0.1)
    def test_case16(self):
       #Title used by Gradescope 
        """Test Case 16: Tests predict_tree_height()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "15"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "25"
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()
    
    @weight(0.1)
    def test_case17(self):
       #Title used by Gradescope 
        """Test Case 17: Tests predict_tree_height()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "16"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "20"
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()
    
    @weight(0.1)
    def test_case18(self):
       #Title used by Gradescope 
        """Test Case 18: Tests predict_tree_height()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "17"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "25"
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()
    
    @weight(0.1)
    def test_case19(self):
       #Title used by Gradescope 
        """Test Case 19: Tests predict_tree_height()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "18"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "-1"
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()
    
    @weight(0.1)
    def test_case20(self):
       #Title used by Gradescope 
        """Test Case 20: Tests predict_tree_height()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "19"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "10"
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()
    
    @weight(0.1)
    def test_case21(self):
       #Title used by Gradescope 
        """Test Case 21: Tests predict_tree_height()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "20"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "15"
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()
    
    @weight(0.1)
    def test_case22(self):
       #Title used by Gradescope 
        """Test Case 22: Tests predict_tree_height()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "21"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "13.5"
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()
    
    @weight(0.1)
    def test_case23(self):
       #Title used by Gradescope 
        """Test Case 23: Tests predict_tree_height()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "22"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "15.125"
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()
    
    @weight(0.1)
    def test_case24(self):
       #Title used by Gradescope 
        """Test Case 24: Tests predict_tree_height()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "23"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "14.1"
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()
    
    @weight(0.1)
    def test_case25(self):
       #Title used by Gradescope 
        """Test Case 25: Tests predict_tree_height()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "24"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "15.25"
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()

    @weight(0.1)
    def test_case26(self):
       #Title used by Gradescope 
        """Test Case 26: Tests k_wrapped_books()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "25"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "2"
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()
    
    @weight(0.1)
    def test_case27(self):
       #Title used by Gradescope 
        """Test Case 27: Tests k_wrapped_books()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "26"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "2"
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()
    
    @weight(0.1)
    def test_case28(self):
       #Title used by Gradescope 
        """Test Case 28: Tests k_wrapped_books()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "27"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "-1"
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()
    
    @weight(0.1)
    def test_case29(self):
       #Title used by Gradescope 
        """Test Case 29: Tests k_wrapped_books()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "28"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "2"
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()
    
    @weight(0.1)
    def test_case30(self):
       #Title used by Gradescope 
        """Test Case 30: Tests k_wrapped_books()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "29"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "3"
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()
    
    @weight(0.1)
    def test_case31(self):
       #Title used by Gradescope 
        """Test Case 31: Tests k_wrapped_books()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "30"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "-1"
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()
    
    @weight(0.1)
    def test_case32(self):
       #Title used by Gradescope 
        """Test Case 32: Tests k_wrapped_books()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "31"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "4"
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()
    
    @weight(0.1)
    def test_case33(self):
       #Title used by Gradescope 
        """Test Case 33: Tests k_wrapped_books()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "32"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "4"
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()
    
    @weight(0.1)
    def test_case34(self):
       #Title used by Gradescope 
        """Test Case 34: Tests k_wrapped_books()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "33"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "-1"
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()
    
    @weight(0.1)
    def test_case35(self):
       #Title used by Gradescope 
        """Test Case 35: Tests k_wrapped_books()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "34"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "2"
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()
    
    @weight(0.1)
    def test_case36(self):
       #Title used by Gradescope 
        """Test Case 36: Tests k_wrapped_books()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "35"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "3"
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()
    
    @weight(0.1)
    def test_case37(self):
       #Title used by Gradescope 
        """Test Case 37: Tests k_wrapped_books()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "36"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "3"
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()
    
    @weight(0.1)
    def test_case38(self):
       #Title used by Gradescope 
        """Test Case 38: Tests k_wrapped_books()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "37"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "4"
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()
    
    @weight(0.1)
    def test_case39(self):
       #Title used by Gradescope 
        """Test Case 39: Tests k_wrapped_books()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "38"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "2"
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()
    
    @weight(0.1)
    def test_case40(self):
       #Title used by Gradescope 
        """Test Case 40: Tests k_wrapped_books()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "39"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "3"
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()
    
    @weight(0.1)
    def test_case41(self):
       #Title used by Gradescope 
        """Test Case 41: Tests k_wrapped_books()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "40"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "4"
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()
    
    @weight(0.1)
    def test_case42(self):
       #Title used by Gradescope 
        """Test Case 42: Tests k_wrapped_books()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "41"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "4"
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()
    
    @weight(0.1)
    def test_case43(self):
       #Title used by Gradescope 
        """Test Case 43: Tests k_wrapped_books()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "42"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "6"
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()
    
    @weight(0.1)
    def test_case44(self):
       #Title used by Gradescope 
        """Test Case 44: Tests k_wrapped_books()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "43"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "-1"
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()
    
    @weight(0.1)
    def test_case45(self):
       #Title used by Gradescope 
        """Test Case 45: Tests k_wrapped_books()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "44"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "2"
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()
    
    @weight(0.1)
    def test_case46(self):
       #Title used by Gradescope 
        """Test Case 46: Tests k_wrapped_books()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "45"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "3"
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()
    
    @weight(0.1)
    def test_case47(self):
       #Title used by Gradescope 
        """Test Case 47: Tests k_wrapped_books()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "46"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "3"
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()
    
    @weight(0.1)
    def test_case48(self):
       #Title used by Gradescope 
        """Test Case 48: Tests k_wrapped_books()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "47"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "5"
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()
    
    @weight(0.1)
    def test_case49(self):
       #Title used by Gradescope 
        """Test Case 49: Tests k_wrapped_books()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "48"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "-1"
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()
    
    @weight(0.1)
    def test_case50(self):
       #Title used by Gradescope 
        """Test Case 50: Tests k_wrapped_books()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "49"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "2"
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()
    
    @weight(0.1)
    def test_case51(self):
       #Title used by Gradescope 
        """Test Case 51: Tests rearrange_bracelet()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "50"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        message = "Did not find a valid rearrangement"
        # Standard unit test case with an associated error message 
        self.assertIn(output, ['cabcab', 'abcabc', 'bacbac', 'bcabca', 'cbacba', 'acbacb'], msg=message)
        test.terminate()
    
    @weight(0.1)
    def test_case52(self):
       #Title used by Gradescope 
        """Test Case 52: Tests rearrange_bracelet()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "51"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        message = "Did not find a valid rearrangement"
        # Standard unit test case with an associated error message 
        self.assertEqual(output,"", msg=message)
        test.terminate()
    
    @weight(0.1)
    def test_case53(self):
       #Title used by Gradescope 
        """Test Case 53: Tests rearrange_bracelet()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "52"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        message = "Did not find a valid rearrangement"
        # Standard unit test case with an associated error message 
        self.assertIn(output, ['egefe', 'efege'], msg=message)
        test.terminate()
    
    @weight(0.1)
    def test_case54(self):
       #Title used by Gradescope 
        """Test Case 54: Tests rearrange_bracelet()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "53"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        message = "Did not find a valid rearrangement"
        # Standard unit test case with an associated error message 
        self.assertIn(output, ['abcadbac', 'abdcabca', 'acbdabca', 'acbdacba', 'abcadbca', 'abcadcab', 'bacbacda', 'bacbadca', 'acdabcab', 'adbacbac', 'acbadcba', 'abdacbac', 'abcadcba', 'acdbacba', 'acbacdab', 'abcdabca', 'cabdabca', 'acbacbad', 'adcabcab', 'acbadbac', 'cabcabda', 'dacbacba', 'acbacbda', 'abcabcad', 'acbadbca', 'adcbacba', 'abcabcda', 'bacdacba', 'abcdacba', 'dabcabca', 'abcabdac', 'acbadcab', 'adbcabca', 'cabdacba', 'acbacdba', 'cadbacba', 'cabcadba', 'abcabdca', 'badcabca', 'bacdabca'], msg=message)
        test.terminate()
    
    @weight(0.1)
    def test_case55(self):
       #Title used by Gradescope 
        """Test Case 55: Tests rearrange_bracelet()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "54"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        message = "Did not find a valid rearrangement"
        # Standard unit test case with an associated error message 
        self.assertIn(output, ['cbacba', 'cbabca', 'cbcaba', 'bacacb', 'babcac', 'acbacb', 'acbcba', 'acbabc', 'abcbac', 'abcacb', 'bacbca', 'cacbab', 'bacabc', 'cbabac', 'bacbac', 'bcacab', 'bcabac', 'cabcab', 'abacbc', 'abcabc', 'cabacb', 'bcacba', 'acabcb', 'bcbaca', 'bcabca', 'abcbca', 'acbcab', 'cabcba', 'cababc', 'cbacab'], msg=message)
        test.terminate()
    
    @weight(0.1)
    def test_case56(self):
       #Title used by Gradescope 
        """Test Case 56: Tests rearrange_bracelet()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "55"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        message = "Did not find a valid rearrangement"
        # Standard unit test case with an associated error message 
        self.assertIn(output, ['bdbebdc', 'bcbdedb', 'dbdcbeb', 'dbcbedb', 'bdbecdb', 'cdbdbeb', 'dcbebdb', 'bdcdbeb', 'dbcdbeb', 'bdebcbd', 'bdbecbd', 'debdbcb', 'dbcebdb', 'cbdbebd', 'bcdbebd', 'cebdbdb', 'cbdebdb', 'cbdbedb', 'ebdcbdb', 'bcebdbd', 'cbedbdb', 'bdbcdeb', 'edbcbdb', 'bebdbcd', 'bdbcbed', 'dbecbdb', 'bdbcedb', 'dbebcbd', 'bdcbdbe', 'ebcbdbd', 'bcbdbde', 'bdedbcb', 'dbdbecb', 'cdbebdb', 'dbdbcbe', 'bdbdecb', 'ebdbcbd', 'debcbdb', 'bcedbdb', 'ecbdbdb', 'bdcebdb', 'bedbcdb', 'bebcdbd', 'bedcbdb', 'bdecbdb', 'dbebdbc', 'bcdebdb', 'bcbedbd', 'ebdbdbc', 'bcbdbed', 'bebdcbd', 'bdcbdeb', 'bdbdcbe', 'dbdbceb', 'dbdebcb', 'ebdbcdb', 'cbdbdbe', 'bdbcbde', 'bcbdebd', 'bdbebcd', 'dcbdbeb', 'cbdbdeb', 'bdbedcb', 'dbcbebd', 'edbdbcb', 'becdbdb', 'bdbdebc', 'bedbdcb', 'dbedbcb', 'bdebdcb', 'bebdbdc', 'bedbcbd', 'dbebdcb', 'bdbcdbe', 'becbdbd', 'bdbdceb', 'dbebcdb', 'bdcbedb', 'cbebdbd', 'dbcbdeb', 'bedbdbc', 'bebdcdb', 'dbcbdbe', 'ebcdbdb', 'bdbcebd', 'ebdbdcb', 'bdebcdb', 'bdebdbc', 'bdbdbce', 'bdcbebd', 'bdbdbec', 'bcdbdeb', 'dbdbebc', 'bdbedbc', 'bcdbdbe', 'bcdbedb'], msg=message)
        test.terminate()
    
    @weight(0.1)
    def test_case57(self):
       #Title used by Gradescope 
        """Test Case 57: Tests rearrange_bracelet()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "56"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        message = "Did not find a valid rearrangement"
        # Standard unit test case with an associated error message 
        self.assertIn(output, ['bcdbedb', 'bdebcdb', 'bdebdcb', 'bdcbdeb', 'bedbcdb', 'bdcbedb'], msg=message)
        test.terminate()
    
    @weight(0.1)
    def test_case58(self):
       #Title used by Gradescope 
        """Test Case 58: Tests rearrange_bracelet()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "57"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        message = "Did not find a valid rearrangement"
        # Standard unit test case with an associated error message 
        self.assertIn(output, ['becdbecdb', 'bcedbcedb', 'bdecbdecb', 'bdcebdceb', 'bcdebcdeb', 'bedcbedcb'], msg=message)
        test.terminate()
    
    @weight(0.1)
    def test_case59(self):
       #Title used by Gradescope 
        """Test Case 59: Tests rearrange_bracelet()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "58"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        message = "Did not find a valid rearrangement"
        # Standard unit test case with an associated error message 
        self.assertIn(output, ['abjbaja', 'jajbaba', 'ajabjab', 'ajbajba', 'abjabja', 'bajajba', 'ajbjaba', 'ajabajb', 'ababjaj', 'ajbabaj', 'bjabaja', 'jabajab', 'bajabja', 'jababja', 'bajabaj', 'ajbajab', 'ajabjba', 'abjajab', 'abjajba', 'jababaj', 'babajaj', 'ajajbab', 'abajajb', 'ajababj', 'jabjaba', 'jajabab', 'babjaja', 'jbabaja', 'abajabj', 'jbajaba', 'jabajba', 'ajbabja', 'abajbja', 'bajajab', 'bjajaba', 'abjabaj', 'abajbaj', 'bajbaja'], msg=message)
        test.terminate()
    
    @weight(0.1)
    def test_case60(self):
       #Title used by Gradescope 
        """Test Case 60: Tests rearrange_bracelet()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "59"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        message = "Did not find a valid rearrangement"
        # Standard unit test case with an associated error message 
        self.assertIn(output, ['ajbajba', 'abjabja'], msg=message)
        test.terminate()
    
    @weight(0.1)
    def test_case61(self):
       #Title used by Gradescope 
        """Test Case 61: Tests rearrange_bracelet()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "60"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        message = "Did not find a valid rearrangement"
        # Standard unit test case with an associated error message 
        self.assertIn(output, ['jkfjkfjk', 'kjfkjfkj'], msg=message)
        test.terminate()
    
    @weight(0.1)
    def test_case62(self):
       #Title used by Gradescope 
        """Test Case 62: Tests rearrange_bracelet()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "61"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        message = "Did not find a valid rearrangement"
        # Standard unit test case with an associated error message 
        self.assertIn(output, ['jkjfjkfk', 'fjkfjkjk', 'kjfkjkfj', 'jkjkfkfj', 'fkfjkjkj', 'kfjkjkjf', 'kjkfjkfj', 'jkfjkfkj', 'kjfjkjkf', 'fkjkjfjk', 'jkfkjfjk', 'kfkjfjkj', 'jkfjkjkf', 'jfkjkjkf', 'jfkjkfjk', 'kjfjfkjk', 'kfjkjfjk', 'kfjkjkfj', 'fjkjkfjk', 'kjkfjkjf', 'fkjkjkjf', 'kjfjkfjk', 'jkjkfjkf', 'jfkjkfkj', 'fjkjkjfk', 'jfjkjkfk', 'kjkfjfkj', 'jkfkfjkj', 'jfkfkjkj', 'kfjkfjkj', 'jfjkfkjk', 'kjkjfkjf', 'jkjfkfjk', 'jkjfkfkj', 'fkjkjfkj', 'jkjkjfkf', 'jkfkjkjf', 'kfkjkjfj', 'kjfkjfkj', 'kjkjfjfk', 'kfjfjkjk', 'fjkfkjkj', 'kfjkjfkj', 'fkjkjkfj', 'kjkjkfjf', 'jkfjfkjk', 'kjfjkfkj', 'kfjfkjkj', 'fkjkfjkj', 'fkjfjkjk', 'fkjfkjkj', 'kjkjfkfj', 'jkfjkjfk', 'jkjfkjfk', 'jfkfjkjk', 'jfkjkjfk', 'jkjfkjkf', 'jkjkfkjf', 'jkfkjfkj', 'fjkjkfkj', 'kjfjkjfk', 'kjfkjkjf', 'fjkjkjkf', 'fjkjfkjk', 'fjfkjkjk', 'kjfkfjkj', 'kjkfjfjk', 'kjkfkjfj', 'jkjkfjfk', 'jkfkjkfj', 'jkfjkfjk', 'jfkjfkjk', 'kjkjfjkf', 'kjfkjfjk'], msg=message)
        test.terminate()
    
    @weight(0.1)
    def test_case63(self):
       #Title used by Gradescope 
        """Test Case 63: Tests rearrange_bracelet()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "62"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        message = "Did not find a valid rearrangement"
        # Standard unit test case with an associated error message 
        self.assertIn(output, ['wgspgwp', 'spgwpgw', 'gwpswpg', 'pwgpsgw', 'gpwspwg', 'wpgspwg', 'pgwpsgw', 'wsgpwgp', 'pwsgwpg', 'wgpwgsp', 'wpgswpg', 'pwgpswg', 'pwgpwgs', 'pwgspwg', 'swpgwpg', 'sgpwgpw', 'pgwpgws', 'gpwgpsw', 'gpwgspw', 'pgwpswg', 'gwpswgp', 'pgswgpw', 'gpwspgw', 'wpgwpgs', 'wgspwgp', 'swgpwgp', 'pwgswpg', 'pwgpwsg', 'gwpgwsp', 'gwspgwp', 'pgwpgsw', 'wgpswpg', 'pgswpgw', 'pwsgpwg', 'gwpsgpw', 'wspgwpg', 'gwpgspw', 'pwgswgp', 'gspwgpw', 'wpgwsgp', 'pgwsgwp', 'pgwsgpw', 'gwpsgwp', 'wgpwsgp', 'gswpgwp', 'wpsgpwg', 'psgwpgw', 'wgpswgp', 'wpgspgw', 'gpwsgwp', 'gwpgswp', 'gwspwgp', 'pwgspgw', 'wgpsgpw', 'pswgpwg', 'gpwgswp', 'gpwsgpw', 'wgpwgps', 'pgwspwg', 'gwpgwps', 'gpswgpw', 'wpgwpsg', 'wgpsgwp', 'wpgswgp', 'wgpwspg', 'pgwspgw', 'gpswpgw', 'spwgpwg', 'sgwpgwp', 'gpwgpws', 'wpgwspg', 'wpsgwpg'], msg=message)
        test.terminate()
    
    @weight(0.1)
    def test_case64(self):
       #Title used by Gradescope 
        """Test Case 64: Tests rearrange_bracelet()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "63"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        message = "Did not find a valid rearrangement"
        # Standard unit test case with an associated error message 
        self.assertIn(output, ['wpgswpg', 'pwgspwg', 'gwpsgwp', 'wgpswgp', 'gpwsgpw', 'pgwspgw'], msg=message)
        test.terminate()
    
    @weight(0.1)
    def test_case65(self):
       #Title used by Gradescope 
        """Test Case 65: Tests rearrange_bracelet()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "64"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        message = "Did not find a valid rearrangement"
        # Standard unit test case with an associated error message 
        self.assertEqual(output,"", msg=message)
        test.terminate()
    
    @weight(0.1)
    def test_case66(self):
       #Title used by Gradescope 
        """Test Case 66: Tests rearrange_bracelet()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "65"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        message = "Did not find a valid rearrangement"
        # Standard unit test case with an associated error message 
        self.assertIn(output, ['wtigawti', 'witgawit', 'tiwgatiw', 'twigatwi', 'wtiagwti', 'iwtgaiwt', 'itwagitw', 'twiagtwi', 'itwgaitw', 'tiwagtiw', 'iwtagiwt', 'witagwit'], msg=message)
        test.terminate()
    
    @weight(0.1)
    def test_case67(self):
       #Title used by Gradescope 
        """Test Case 67: Tests rearrange_bracelet()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "66"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        message = "Did not find a valid rearrangement"
        # Standard unit test case with an associated error message 
        self.assertIn(output, ['bcbcaj', 'jbcbca', 'cabjbc', 'bcbjac', 'cabcjb', 'cabjcb', 'jbcabc', 'cbcjab', 'bcabcj', 'cbabjc', 'cajbcb', 'bcbjca', 'babcjc', 'jcbacb', 'bcajbc', 'ajbcbc', 'bjacbc', 'cjbacb', 'jcbcba', 'bcjabc', 'cbjcba', 'cabcbj', 'bcbcja', 'cjbcba', 'abcbjc', 'jacbcb', 'cbjacb', 'abcbcj', 'bcacbj', 'bcabjc', 'bacbjc', 'abcjcb', 'jbcbac', 'bjcabc', 'bjcbca', 'bcjbca', 'jcbabc', 'bacjbc', 'cbcabj', 'cbcbaj', 'cbcajb', 'bjbcac', 'acbcjb', 'cjcbab', 'acbcbj', 'acjbcb', 'cbacjb', 'jcabcb', 'bjcbac', 'abcjbc', 'cjabcb', 'jbacbc', 'bajcbc', 'ajcbcb', 'bjcacb', 'cacbjb', 'bcbacj', 'bcbajc', 'cjbabc', 'abjcbc', 'cbajbc', 'cbajcb', 'bcajcb', 'cbacbj', 'jabcbc', 'bcjacb', 'cbjabc', 'bcacjb', 'bacbcj', 'bacjcb', 'cjbcab', 'cbjbac', 'bcjcba', 'jcbcab', 'cbabcj', 'acbjbc', 'cbcbja', 'cbjcab', 'cbjbca', 'cbcjba', 'bcjbac', 'bcjcab', 'jbcacb', 'acbjcb'], msg=message)
        test.terminate()
    
    @weight(0.1)
    def test_case68(self):
       #Title used by Gradescope 
        """Test Case 68: Tests rearrange_bracelet()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "67"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        message = "Did not find a valid rearrangement"
        # Standard unit test case with an associated error message 
        self.assertIn(output, ['cbajbc', 'cbjcab', 'jcbacb', 'cbjcba', 'bacbjc', 'cjbacb', 'cabjcb', 'bcjbca', 'cjbcab', 'jbcabc', 'cbacbj', 'bjcabc', 'cbjacb', 'bcajcb', 'bcjabc', 'bcajbc', 'cabcjb', 'bacjbc', 'bcjbac', 'cbjabc', 'bcabjc', 'bcabcj', 'bjcbac', 'cbacjb', 'bcjacb', 'abcjbc', 'cbajcb', 'acbjcb'], msg=message)
        test.terminate()
    
    @weight(0.1)
    def test_case69(self):
       #Title used by Gradescope 
        """Test Case 69: Tests rearrange_bracelet()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "68"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        message = "Did not find a valid rearrangement"
        # Standard unit test case with an associated error message 
        self.assertIn(output, ['bcjabc', 'cbajcb', 'cbjacb', 'bcajbc'], msg=message)
        test.terminate()
    
    @weight(0.1)
    def test_case70(self):
       #Title used by Gradescope 
        """Test Case 70: Tests rearrange_bracelet()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "69"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        message = "Did not find a valid rearrangement"
        # Standard unit test case with an associated error message 
        self.assertEqual(output,"", msg=message)
        test.terminate()
    
    @weight(0.1)
    def test_case71(self):
       #Title used by Gradescope 
        """Test Case 71: Tests rearrange_bracelet()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "70"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        message = "Did not find a valid rearrangement"
        # Standard unit test case with an associated error message 
        self.assertIn(output, ['ghghghj', 'gjhghgh', 'hghjghg', 'jghghgh', 'ghgjhgh', 'ghghjgh', 'hjghghg', 'hghghjg', 'hghghgj', 'hgjhghg', 'hghgjgh', 'ghghjhg', 'hgjghgh', 'hghgjhg', 'ghghgjh', 'ghjghgh', 'jhghghg', 'ghjhghg'], msg=message)
        test.terminate()
    
    @weight(0.1)
    def test_case72(self):
       #Title used by Gradescope 
        """Test Case 72: Tests rearrange_bracelet()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "71"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        message = "Did not find a valid rearrangement"
        # Standard unit test case with an associated error message 
        self.assertIn(output, ['jnklmj', 'jknlmj', 'kjlnmj', 'jnkmjl', 'mjklnj', 'jmnljk', 'mjnklj', 'kjlmnj', 'jlkmjn', 'jlnkmj', 'jknmjl', 'mjlknj', 'jmknjl', 'njklmj', 'jlnmjk', 'ljknmj', 'ljkmnj', 'jmklnj', 'jklnjm', 'jlnmkj', 'jmlnjk', 'jklmnj', 'jkmljn', 'jklmjn', 'jnmklj', 'jkmnlj', 'jmknlj', 'jnlkmj', 'jmnklj', 'njmklj', 'njlkmj', 'njkmlj', 'jlkmnj', 'jmnlkj', 'jnlmjk', 'jkmnjl', 'ljnkmj', 'jnkljm', 'jlmkjn', 'mjknlj', 'jlmknj', 'jlknmj', 'jnmljk', 'jlmnkj', 'jlknjm', 'ljmknj', 'jmkljn', 'jnkmlj', 'mjlnkj', 'ljmnkj', 'njlmkj', 'njmlkj', 'jmnkjl', 'jnmlkj', 'jkmlnj', 'kjnmlj', 'jlnkjm', 'jnmkjl', 'jklnmj', 'kjmlnj', 'jnlkjm', 'jnlmkj', 'ljnmkj', 'mjnlkj', 'jmlkjn', 'jknljm', 'kjmnlj', 'kjnlmj', 'jknmlj', 'jmlnkj', 'jmlknj', 'jlmnjk'], msg=message)
        test.terminate()
    
    @weight(0.1)
    def test_case73(self):
       #Title used by Gradescope 
        """Test Case 73: Tests rearrange_bracelet()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "72"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        message = "Did not find a valid rearrangement"
        # Standard unit test case with an associated error message 
        self.assertIn(output, ['jkmlnj', 'jnmklj', 'jknmlj', 'jklnmj', 'jmklnj', 'jlnkmj', 'jklmnj', 'jkmnlj', 'jnlmkj', 'jmlknj', 'jlkmnj', 'jlmnkj', 'jmlnkj', 'jlknmj', 'jknlmj', 'jmnklj', 'jnkmlj', 'jnmlkj', 'jmnlkj', 'jlmknj', 'jmknlj', 'jlnmkj', 'jnlkmj', 'jnklmj'], msg=message)
        test.terminate()
    
    @weight(0.1)
    def test_case74(self):
       #Title used by Gradescope 
        """Test Case 74: Tests rearrange_bracelet()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "73"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        message = "Did not find a valid rearrangement"
        # Standard unit test case with an associated error message 
        self.assertIn(output, ['jkcnlmj', 'jcmlknj', 'jnmclkj', 'jcnkmlj', 'jcmnklj', 'jmlnkcj', 'jckmlnj', 'jlcknmj', 'jmcklnj', 'jnmklcj', 'jckmnlj', 'jkcnmlj', 'jncmklj', 'jmclknj', 'jnlkmcj', 'jmklncj', 'jmknlcj', 'jncmlkj', 'jlnkmcj', 'jcmlnkj', 'jcnlkmj', 'jnclmkj', 'jmnklcj', 'jnmlkcj', 'jknlcmj', 'jmknclj', 'jlnckmj', 'jklcmnj', 'jnmcklj', 'jkcmlnj', 'jknclmj', 'jknmlcj', 'jmnlkcj', 'jlknmcj', 'jnlmckj', 'jlkncmj', 'jnklmcj', 'jlckmnj', 'jmnclkj', 'jklcnmj', 'jmklcnj', 'jmncklj', 'jmcnklj', 'jknmclj', 'jkclmnj', 'jklmcnj', 'jncklmj', 'jnlckmj', 'jmkcnlj', 'jlmkncj', 'jclnkmj', 'jklnmcj', 'jcmnlkj', 'jmkclnj', 'jkmnlcj', 'jcnmlkj', 'jlmnkcj', 'jlmcknj', 'jnklcmj', 'jlnkcmj', 'jclnmkj', 'jnkmlcj', 'jnlkcmj', 'jlmnckj', 'jmnlckj', 'jkmclnj', 'jcmklnj', 'jkmcnlj', 'jnkmclj', 'jklncmj', 'jlcmnkj', 'jknlmcj', 'jlmcnkj', 'jlcnmkj', 'jmcknlj', 'jnckmlj', 'jnmlckj', 'jmcnlkj', 'jnlcmkj', 'jmclnkj', 'jlnmckj', 'jkncmlj', 'jnkcmlj', 'jnkclmj', 'jlkcmnj', 'jcklnmj', 'jcmknlj', 'jmnkclj', 'jlkcnmj', 'jlncmkj', 'jclkmnj', 'jclknmj', 'jcnklmj', 'jclmnkj', 'jnlmkcj', 'jkmlcnj', 'jclmknj', 'jlmkcnj', 'jkclnmj', 'jlkmncj', 'jkcmnlj', 'jcnmklj', 'jmlcknj', 'jnclkmj', 'jlcmknj', 'jkmlncj', 'jmlnckj', 'jkmnclj', 'jlcnkmj', 'jlkmcnj', 'jcklmnj', 'jlnmkcj', 'jnmkclj', 'jcknmlj', 'jmlkncj', 'jmlkcnj', 'jcnlmkj', 'jcknlmj', 'jmlcnkj', 'jklmncj'], msg=message)
        test.terminate()
    
    @weight(0.1)
    def test_case75(self):
       #Title used by Gradescope 
        """Test Case 75: Tests rearrange_bracelet()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "74"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        message = "Did not find a valid rearrangement"
        # Standard unit test case with an associated error message 
        self.assertIn(output, ['ygtwfyg', 'ygwtfyg', 'gytwfgy', 'ygwftyg', 'gywftgy', 'ygftwyg', 'ygtfwyg', 'gytfwgy', 'ygfwtyg', 'gyftwgy', 'gywtfgy', 'gyfwtgy'], msg=message)
        test.terminate()
    
    @weight(0.1)
    def test_case76(self):
       #Title used by Gradescope 
        """Test Case 76: Tests second_longest_prefix()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "75"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "s"
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()
    
    @weight(0.1)
    def test_case77(self):
       #Title used by Gradescope 
        """Test Case 77: Tests second_longest_prefix()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "76"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "ab"
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()
    
    @weight(0.1)
    def test_case78(self):
       #Title used by Gradescope 
        """Test Case 78: Tests second_longest_prefix()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "77"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = ""
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()
    
    @weight(0.1)
    def test_case79(self):
       #Title used by Gradescope 
        """Test Case 79: Tests second_longest_prefix()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "78"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "aaa"
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()
    
    @weight(0.1)
    def test_case80(self):
       #Title used by Gradescope 
        """Test Case 80: Tests second_longest_prefix()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "79"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "a"
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()
    
    @weight(0.1)
    def test_case81(self):
       #Title used by Gradescope 
        """Test Case 81: Tests second_longest_prefix()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "80"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = ""
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()
    
    @weight(0.1)
    def test_case82(self):
       #Title used by Gradescope 
        """Test Case 82: Tests second_longest_prefix()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "81"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "ababab"
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()
    
    @weight(0.1)
    def test_case83(self):
       #Title used by Gradescope 
        """Test Case 83: Tests second_longest_prefix()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "82"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "abab"
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()
    
    @weight(0.1)
    def test_case84(self):
       #Title used by Gradescope 
        """Test Case 84: Tests second_longest_prefix()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "83"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "ab"
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()
    
    @weight(0.1)
    def test_case85(self):
       #Title used by Gradescope 
        """Test Case 85: Tests second_longest_prefix()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "84"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "b"
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()
    
    @weight(0.1)
    def test_case86(self):
       #Title used by Gradescope 
        """Test Case 86: Tests second_longest_prefix()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "85"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "ba"
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()
    
    @weight(0.1)
    def test_case87(self):
       #Title used by Gradescope 
        """Test Case 87: Tests second_longest_prefix()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "86"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = ""
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()
    
    @weight(0.1)
    def test_case88(self):
       #Title used by Gradescope 
        """Test Case 88: Tests second_longest_prefix()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "87"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "bb"
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()
    
    @weight(0.1)
    def test_case89(self):
       #Title used by Gradescope 
        """Test Case 89: Tests second_longest_prefix()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "88"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "b"
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()
    
    @weight(0.1)
    def test_case90(self):
       #Title used by Gradescope 
        """Test Case 90: Tests second_longest_prefix()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "89"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = ""
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()
    
    @weight(0.1)
    def test_case91(self):
       #Title used by Gradescope 
        """Test Case 91: Tests second_longest_prefix()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "90"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "bbbb"
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()
    
    @weight(0.1)
    def test_case92(self):
       #Title used by Gradescope 
        """Test Case 92: Tests second_longest_prefix()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "91"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "b"
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()
    
    @weight(0.1)
    def test_case93(self):
       #Title used by Gradescope 
        """Test Case 93: Tests second_longest_prefix()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "92"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = ""
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()
    
    @weight(0.1)
    def test_case94(self):
       #Title used by Gradescope 
        """Test Case 94: Tests second_longest_prefix()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "93"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "a"
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()
    
    @weight(0.1)
    def test_case95(self):
       #Title used by Gradescope 
        """Test Case 95: Tests second_longest_prefix()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "94"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "ffg"
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()
    
    @weight(0.1)
    def test_case96(self):
       #Title used by Gradescope 
        """Test Case 96: Tests second_longest_prefix()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "95"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = ""
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()
    
    @weight(0.1)
    def test_case97(self):
       #Title used by Gradescope 
        """Test Case 97: Tests second_longest_prefix()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "96"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = ""
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()
    
    @weight(0.1)
    def test_case98(self):
       #Title used by Gradescope 
        """Test Case 98: Tests second_longest_prefix()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "97"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "c"
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()
    
    @weight(0.1)
    def test_case99(self):
       #Title used by Gradescope 
        """Test Case 99: Tests second_longest_prefix()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "98"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = ""
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()
    
    @weight(0.1)
    def test_case100(self):
       #Title used by Gradescope 
        """Test Case 100: Tests second_longest_prefix()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "99"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "j"
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()

    runTime = time.time() - start_time

  

   