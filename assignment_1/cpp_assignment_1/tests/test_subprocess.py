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
    @weight(5)
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
    @weight(15)
    def test_case1(self):
        #Title used by Gradescope 
        """Test Case 1"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "0"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        errorMessage = "Expected: True\nFound: "+output
        # Standard unit test case with an associated error message 
        self.assertTrue( output == "True", msg=output)
        test.terminate()
    
    # Associated point value within GradeScope
    @weight(20)
    def test_case2(self):
        # Title used by Gradescope 
        """Test Case 2"""

       # Create a subprocess to run the students code with the Second Command Line Option
        test = subprocess.Popen(["./test.out", "1"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        errorMessage = "Expected: False\nFound: "+output
        # Standard unit test case with an associated error message 
        self.assertTrue( output == "False", msg=output)
        test.terminate()

    # Associated point value within GradeScope
    @weight(20)
    def test_case3(self):
        # Title used by Gradescope 
        """Test Case 3"""

        # Create a subprocess to run the students code with the Third Command Line Option
        test = subprocess.Popen(["./test.out", "2"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        errorMessage = "Expected: True\nFound: "+output
        # Standard unit test case with an associated error message 
        self.assertTrue( output == "True", msg=output)
        test.terminate()
    
    @weight(20)
    def test_case4(self):
        # Title used by Gradescope 
        """Test Case 4"""

        # Create a subprocess to run the students code with the Third Command Line Option
        test = subprocess.Popen(["./test.out", "3"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        errorMessage = "Expected: True\nFound: "+output
        # Standard unit test case with an associated error message 
        self.assertTrue( output == "True", msg=output)
        test.terminate()
    
    @weight(20)
    def test_case5(self):
        # Title used by Gradescope 
        """Test Case 5"""

        # Create a subprocess to run the students code with the Third Command Line Option
        test = subprocess.Popen(["./test.out", "4"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        errorMessage = "Expected: True\nFound: "+output
        # Standard unit test case with an associated error message 
        self.assertTrue( output == "True", msg=output)
        test.terminate()
    
    runTime = time.time() - start_time

  

   