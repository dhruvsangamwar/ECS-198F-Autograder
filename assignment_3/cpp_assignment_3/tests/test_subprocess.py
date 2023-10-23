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
    @weight(10)
    def test_case1(self):
        #Title used by Gradescope 
        """Test Case 1"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "0"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        errorMessage = "Expected: 4\nFound: "+output
        # Standard unit test case with an associated error message 
        self.assertTrue( output == "4", msg=output)
        test.terminate()
    
    # Associated point value within GradeScope
    @weight(10)
    def test_case2(self):
        # Title used by Gradescope 
        """Test Case 2"""

       # Create a subprocess to run the students code with the Second Command Line Option
        test = subprocess.Popen(["./test.out", "1"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        errorMessage = "Expected: False\nFound: "+output
        # Standard unit test case with an associated error message 
        self.assertTrue( output == "3", msg=output)
        test.terminate()

    # Associated point value within GradeScope
    @weight(10)
    def test_case3(self):
        # Title used by Gradescope 
        """Test Case 3"""

        # Create a subprocess to run the students code with the Third Command Line Option
        test = subprocess.Popen(["./test.out", "2"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        errorMessage = "Expected: True\nFound: "+output
        # Standard unit test case with an associated error message 
        self.assertTrue( output == "3", msg=output)
        test.terminate()
    
    @weight(10)
    def test_case4(self):
        # Title used by Gradescope 
        """Test Case 4"""

        # Create a subprocess to run the students code with the Third Command Line Option
        test = subprocess.Popen(["./test.out", "3"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        errorMessage = "Expected: True\nFound: "+output
        # Standard unit test case with an associated error message 
        self.assertTrue( output == "5", msg=output)
        test.terminate()
    
    @weight(10)
    def test_case5(self):
        # Title used by Gradescope 
        """Test Case 5"""

        # Create a subprocess to run the students code with the Third Command Line Option
        test = subprocess.Popen(["./test.out", "4"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        errorMessage = "Expected: True\nFound: "+output
        # Standard unit test case with an associated error message 
        self.assertTrue( output == "4", msg=output)
        test.terminate()
    
    @weight(10)
    def test_case6(self):
        # Title used by Gradescope 
        """Test Case 6"""

        # Create a subprocess to run the students code with the Third Command Line Option
        test = subprocess.Popen(["./test.out", "5"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        errorMessage = "Expected: 1\nFound: "+output
        # Standard unit test case with an associated error message 
        self.assertTrue( output == "1", msg=output)
        test.terminate()

    @weight(10)
    def test_case7(self):
        # Title used by Gradescope 
        """Test Case 7"""

        # Create a subprocess to run the students code with the Third Command Line Option
        test = subprocess.Popen(["./test.out", "6"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        errorMessage = "Expected: 1 2 3 4 -1\nFound: "+output
        # Standard unit test case with an associated error message 
        self.assertTrue( output == "1 2 3 4 -1", msg=output)
        test.terminate()

    @weight(10)
    def test_case8(self):
        # Title used by Gradescope 
        """Test Case 8"""

        # Create a subprocess to run the students code with the Third Command Line Option
        test = subprocess.Popen(["./test.out", "7"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        errorMessage = "Expected: 1 -1 3\nFound: "+output
        # Standard unit test case with an associated error message 
        self.assertTrue( output == "1 -1 3", msg=output)
        test.terminate()

    @weight(10)
    def test_case9(self):
        # Title used by Gradescope 
        """Test Case 9"""

        # Create a subprocess to run the students code with the Third Command Line Option
        test = subprocess.Popen(["./test.out", "8"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        errorMessage = "Expected: 1 2 -1\nFound: "+output
        # Standard unit test case with an associated error message 
        self.assertTrue( output == "1 2 -1", msg=output)
        test.terminate()

    @weight(10)
    def test_case10(self):
        # Title used by Gradescope 
        """Test Case 10"""

        # Create a subprocess to run the students code with the Third Command Line Option
        test = subprocess.Popen(["./test.out", "9"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        errorMessage = "Expected: -1 -1\nFound: "+output
        # Standard unit test case with an associated error message 
        self.assertTrue( output == "-1 -1", msg=output)
        test.terminate()


    runTime = time.time() - start_time

  

   