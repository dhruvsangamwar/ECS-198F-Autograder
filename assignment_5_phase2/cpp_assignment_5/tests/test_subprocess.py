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

        expected = ""
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output

        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()

    # Associated point value within GradeScope
    @weight(0)
    def test_case0(self):
        #Title used by Gradescope 
        """Test Case 0 - Making sure Autograder works"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "0"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "Gradescope working properly - should be always correct, please ignore"
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output

        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()

    @weight(0.1)
    def test_case1(self):
        #Title used by Gradescope 
        """Test Case 1: Tests count_scores()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "0"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "YES_NO_NO"
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output

        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()

    @weight(0.1)
    def test_case2(self):
        #Title used by Gradescope 
        """Test Case 2: Tests count_scores()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "0"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "NO_NO_NO_NO_YES"
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output

        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()

    @weight(0.1)
    def test_case3(self):
        #Title used by Gradescope 
        """Test Case 3: Tests count_scores()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "0"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = ""
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output

        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()

    @weight(0.1)
    def test_case4(self):
        #Title used by Gradescope 
        """Test Case 4: Tests count_scores()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "0"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "YES_YES_NO_YES"
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output

        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()

    @weight(0.1)
    def test_case5(self):
        #Title used by Gradescope 
        """Test Case 5: Tests count_scores()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "0"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "YES_NO_NO_NO_NO_NO_YES_YES_NO"
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output

        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()

    @weight(0.1)
    def test_case6(self):
        #Title used by Gradescope 
        """Test Case 6: Tests count_scores()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "0"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "NO_NO_NO_NO_NO_NO_NO_NO_NO"
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output

        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()

    @weight(0.1)
    def test_case7(self):
        #Title used by Gradescope 
        """Test Case 7: Tests count_scores()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "0"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = ""
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output

        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()

    @weight(0.1)
    def test_case8(self):
        #Title used by Gradescope 
        """Test Case 8: Tests count_scores()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "0"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO"
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output

        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()

    @weight(0.1)
    def test_case9(self):
        #Title used by Gradescope 
        """Test Case 9: Tests count_scores()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "0"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES"
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output

        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()

    @weight(0.1)
    def test_case10(self):
        #Title used by Gradescope 
        """Test Case 10: Tests count_scores()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "0"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "YES_YES_YES"
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output

        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()

    @weight(0.1)
    def test_case11(self):
        #Title used by Gradescope 
        """Test Case 11: Tests count_scores()11: Tests count_scores()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "0"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "YES_NO"
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output

        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()

    @weight(0.1)
    def test_case12(self):
        #Title used by Gradescope 
        """Test Case 12: Tests count_scores()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "0"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "YES_YES_YES_YES"
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output

        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()

    @weight(0.1)
    def test_case13(self):
        #Title used by Gradescope 
        """Test Case 13: Tests count_scores()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "0"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "YES_NO"
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output

        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()

    @weight(0.1)
    def test_case14(self):
        #Title used by Gradescope 
        """Test Case 14: Tests count_scores()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "0"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_NO"
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output

        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()


    @weight(0.1)
    def test_case15(self):
        #Title used by Gradescope 
        """Test Case 15: Tests count_scores()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "0"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "YES"
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output

        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()

    @weight(0.1)
    def test_case16(self):
        #Title used by Gradescope 
        """Test Case 16: Tests count_scores()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "0"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "NO_NO_YES_YES_YES_YES_YES_YES_YES_YES"
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output

        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()

    @weight(0.1)
    def test_case17(self):
        #Title used by Gradescope 
        """Test Case 17: Tests count_scores()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "0"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "YES"
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output

        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()

    @weight(0.1)
    def test_case18(self):
        #Title used by Gradescope 
        """Test Case 18: Tests count_scores()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "0"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "NO"
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output

        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()

    @weight(0.1)
    def test_case19(self):
        #Title used by Gradescope 
        """Test Case 19: Tests count_scores()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "0"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "NO"
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output

        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()

    @weight(0.1)
    def test_case20(self):
        #Title used by Gradescope 
        """Test Case 20: Tests count_scores()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "0"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "YES"
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output

        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()

    @weight(0.1)
    def test_case21(self):
        #Title used by Gradescope 
        """Test Case 21: Tests count_scores()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "0"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "NO_NO_NO"
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output

        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()

    @weight(0.1)
    def test_case22(self):
        #Title used by Gradescope 
        """Test Case 22: Tests count_scores()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "0"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "YES_YES_NO_NO_NO_YES_YES_NO_NO_NO_YES_YES_NO_NO_NO_YES_YES_NO_NO_NO"
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output

        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()

    @weight(0.1)
    def test_case23(self):
        #Title used by Gradescope 
        """Test Case 23: Tests count_scores()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "0"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "NO_NO_YES_YES_YES_NO"
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output

        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()

    @weight(0.1)
    def test_case24(self):
        #Title used by Gradescope 
        """Test Case 24: Tests count_scores()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "0"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "NO_YES_NO_NO"
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output

        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()

    @weight(0.1)
    def test_case25(self):
        #Title used by Gradescope 
        """Test Case 25: Tests count_scores()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "0"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "NO_YES_NO_YES_NO_YES_YES_YES_YES_YES"
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output

        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()

    @weight(0.2)
    def test_case26(self):
        #Title used by Gradescope 
        """Test Case 26: Tests count_scores()"""

        # Create a subprocess to run the students code with the first Command Line Option
        test = subprocess.Popen(["./test.out", "0"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "79_1_1"
        message = "Please note that we are only checking for the sum in this test case which we will extract from your answer. Thus, if you have the same sum as the expected answer, the autograder should have marked this as correct even if the rest of the answer differs from the expected answer. We're printing the sequence from both the expected and your answer so you can compare them and use it if needs be (but the sequence is not necessarily unique).\nWe expected this:\n" + expected + "\nWe got this:\n" + output

        expected = expected.split('_')[0]
        output = output.split('_')[0]

        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()
    
    # Associated point value within GradeScope
    @weight(0.2)
    def test_case27(self):
        # Title used by Gradescope 
        """Test Case 27: Tests count_scores()"""

       # Create a subprocess to run the students code with the Second Command Line Option
        test = subprocess.Popen(["./test.out", "1"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "6_1_2_2_1"
        message = "Please note that we are only checking for the sum in this test case which we will extract from your answer. Thus, if you have the same sum as the expected answer, the autograder should have marked this as correct even if the rest of the answer differs from the expected answer. We're printing the sequence from both the expected and your answer so you can compare them and use it if needs be (but the sequence is not necessarily unique).\nWe expected this:\n" + expected + "\nWe got this:\n" + output

        expected = expected.split('_')[0]
        output = output.split('_')[0]
        
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()

    # Associated point value within GradeScope
    @weight(0.2)
    def test_case28(self):
        # Title used by Gradescope 
        """Test Case 28: Tests count_scores()"""

        # Create a subprocess to run the students code with the Third Command Line Option
        test = subprocess.Popen(["./test.out", "2"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "7_1_3_2_1_3_2_4_4"
        message = "Please note that we are only checking for the sum in this test case which we will extract from your answer. Thus, if you have the same sum as the expected answer, the autograder should have marked this as correct even if the rest of the answer differs from the expected answer. We're printing the sequence from both the expected and your answer so you can compare them and use it if needs be (but the sequence is not necessarily unique).\nWe expected this:\n" + expected + "\nWe got this:\n" + output

        expected = expected.split('_')[0]
        output = output.split('_')[0]
        
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()
    
    @weight(0.2)
    def test_case29(self):
        # Title used by Gradescope 
        """Test Case 29: Tests count_scores()"""

        # Create a subprocess to run the students code with the Third Command Line Option
        test = subprocess.Popen(["./test.out", "3"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "8_1_3_2_6_3_5_4_7_5_4_6_1_7_2"
        message = "Please note that we are only checking for the sum in this test case which we will extract from your answer. Thus, if you have the same sum as the expected answer, the autograder should have marked this as correct even if the rest of the answer differs from the expected answer. We're printing the sequence from both the expected and your answer so you can compare them and use it if needs be (but the sequence is not necessarily unique).\nWe expected this:\n" + expected + "\nWe got this:\n" + output

        expected = expected.split('_')[0]
        output = output.split('_')[0]
        
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()
    
    @weight(0.2)
    def test_case30(self):
        # Title used by Gradescope 
        """Test Case 30: Tests count_scores()"""

        # Create a subprocess to run the students code with the Third Command Line Option
        test = subprocess.Popen(["./test.out", "4"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "501_1_1"
        message = "Please note that we are only checking for the sum in this test case which we will extract from your answer. Thus, if you have the same sum as the expected answer, the autograder should have marked this as correct even if the rest of the answer differs from the expected answer. We're printing the sequence from both the expected and your answer so you can compare them and use it if needs be (but the sequence is not necessarily unique).\nWe expected this:\n" + expected + "\nWe got this:\n" + output

        expected = expected.split('_')[0]
        output = output.split('_')[0]
        
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()
    
    @weight(0.2)
    def test_case31(self):
        # Title used by Gradescope 
        """Test Case 31: Tests rename_people()"""

        # Create a subprocess to run the students code with the Third Command Line Option
        test = subprocess.Popen(["./test.out", "5"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "9_1_3_2_2_3_1_4_4_5_5"
        message = "Please note that we are only checking for the sum in this test case which we will extract from your answer. Thus, if you have the same sum as the expected answer, the autograder should have marked this as correct even if the rest of the answer differs from the expected answer. We're printing the sequence from both the expected and your answer so you can compare them and use it if needs be (but the sequence is not necessarily unique).\nWe expected this:\n" + expected + "\nWe got this:\n" + output

        expected = expected.split('_')[0]
        output = output.split('_')[0]
        
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()

    @weight(0.2)
    def test_case32(self):
        # Title used by Gradescope 
        """Test Case 32: Tests rename_people()"""

        # Create a subprocess to run the students code with the Third Command Line Option
        test = subprocess.Popen(["./test.out", "6"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "1_1_1"
        message = "Please note that we are only checking for the sum in this test case which we will extract from your answer. Thus, if you have the same sum as the expected answer, the autograder should have marked this as correct even if the rest of the answer differs from the expected answer. We're printing the sequence from both the expected and your answer so you can compare them and use it if needs be (but the sequence is not necessarily unique).\nWe expected this:\n" + expected + "\nWe got this:\n" + output

        expected = expected.split('_')[0]
        output = output.split('_')[0]
        
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()

    @weight(0.2)
    def test_case33(self):
        # Title used by Gradescope 
        """Test Case 33: Tests rename_people()"""

        # Create a subprocess to run the students code with the Third Command Line Option
        test = subprocess.Popen(["./test.out", "7"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "2_1_1_2_2"
        message = "Please note that we are only checking for the sum in this test case which we will extract from your answer. Thus, if you have the same sum as the expected answer, the autograder should have marked this as correct even if the rest of the answer differs from the expected answer. We're printing the sequence from both the expected and your answer so you can compare them and use it if needs be (but the sequence is not necessarily unique).\nWe expected this:\n" + expected + "\nWe got this:\n" + output

        expected = expected.split('_')[0]
        output = output.split('_')[0]
        
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()

    @weight(0.2)
    def test_case34(self):
        # Title used by Gradescope 
        """Test Case 34: Tests rename_people()"""

        # Create a subprocess to run the students code with the Third Command Line Option
        test = subprocess.Popen(["./test.out", "8"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "1_1_2_2_1"
        message = "Please note that we are only checking for the sum in this test case which we will extract from your answer. Thus, if you have the same sum as the expected answer, the autograder should have marked this as correct even if the rest of the answer differs from the expected answer. We're printing the sequence from both the expected and your answer so you can compare them and use it if needs be (but the sequence is not necessarily unique).\nWe expected this:\n" + expected + "\nWe got this:\n" + output

        expected = expected.split('_')[0]
        output = output.split('_')[0]
        
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()

    @weight(0.2)
    def test_case35(self):
        # Title used by Gradescope 
        """Test Case 35: Tests rename_people()"""

        # Create a subprocess to run the students code with the Third Command Line Option
        test = subprocess.Popen(["./test.out", "9"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "0_1_1_2_2"
        message = "Please note that we are only checking for the sum in this test case which we will extract from your answer. Thus, if you have the same sum as the expected answer, the autograder should have marked this as correct even if the rest of the answer differs from the expected answer. We're printing the sequence from both the expected and your answer so you can compare them and use it if needs be (but the sequence is not necessarily unique).\nWe expected this:\n" + expected + "\nWe got this:\n" + output

        expected = expected.split('_')[0]
        output = output.split('_')[0]
        
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()


    @weight(0.2)
    def test_case36(self):
        # Title used by Gradescope 
        """Test Case 36: Tests rename_people()"""

        # Create a subprocess to run the students code with the Third Command Line Option
        test = subprocess.Popen(["./test.out", "9"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "2_1_1_2_2"
        message = "Please note that we are only checking for the sum in this test case which we will extract from your answer. Thus, if you have the same sum as the expected answer, the autograder should have marked this as correct even if the rest of the answer differs from the expected answer. We're printing the sequence from both the expected and your answer so you can compare them and use it if needs be (but the sequence is not necessarily unique).\nWe expected this:\n" + expected + "\nWe got this:\n" + output

        expected = expected.split('_')[0]
        output = output.split('_')[0]
        
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()

    @weight(0.2)
    def test_case37(self):
        # Title used by Gradescope 
        """Test Case 37: Tests rename_people()"""

        # Create a subprocess to run the students code with the Third Command Line Option
        test = subprocess.Popen(["./test.out", "9"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "3_1_1_2_3_3_2"
        message = "Please note that we are only checking for the sum in this test case which we will extract from your answer. Thus, if you have the same sum as the expected answer, the autograder should have marked this as correct even if the rest of the answer differs from the expected answer. We're printing the sequence from both the expected and your answer so you can compare them and use it if needs be (but the sequence is not necessarily unique).\nWe expected this:\n" + expected + "\nWe got this:\n" + output

        expected = expected.split('_')[0]
        output = output.split('_')[0]
        
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()

    @weight(0.2)
    def test_case38(self):
        # Title used by Gradescope 
        """Test Case 38: Tests rename_people()"""

        # Create a subprocess to run the students code with the Third Command Line Option
        test = subprocess.Popen(["./test.out", "9"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "10_1_8_2_5_3_10_4_1_5_3_6_7_7_6_8_9_9_4_10_2"
        message = "Please note that we are only checking for the sum in this test case which we will extract from your answer. Thus, if you have the same sum as the expected answer, the autograder should have marked this as correct even if the rest of the answer differs from the expected answer. We're printing the sequence from both the expected and your answer so you can compare them and use it if needs be (but the sequence is not necessarily unique).\nWe expected this:\n" + expected + "\nWe got this:\n" + output

        expected = expected.split('_')[0]
        output = output.split('_')[0]
        
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()

    @weight(0.2)
    def test_case39(self):
        # Title used by Gradescope 
        """Test Case 39: Tests rename_people()"""

        # Create a subprocess to run the students code with the Third Command Line Option
        test = subprocess.Popen(["./test.out", "9"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "0_1_1"
        message = "Please note that we are only checking for the sum in this test case which we will extract from your answer. Thus, if you have the same sum as the expected answer, the autograder should have marked this as correct even if the rest of the answer differs from the expected answer. We're printing the sequence from both the expected and your answer so you can compare them and use it if needs be (but the sequence is not necessarily unique).\nWe expected this:\n" + expected + "\nWe got this:\n" + output

        expected = expected.split('_')[0]
        output = output.split('_')[0]
        
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()

    @weight(0.2)
    def test_case40(self):
        # Title used by Gradescope 
        """Test Case 40: Tests rename_people()"""

        # Create a subprocess to run the students code with the Third Command Line Option
        test = subprocess.Popen(["./test.out", "9"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "2_1_1"
        message = "Please note that we are only checking for the sum in this test case which we will extract from your answer. Thus, if you have the same sum as the expected answer, the autograder should have marked this as correct even if the rest of the answer differs from the expected answer. We're printing the sequence from both the expected and your answer so you can compare them and use it if needs be (but the sequence is not necessarily unique).\nWe expected this:\n" + expected + "\nWe got this:\n" + output

        expected = expected.split('_')[0]
        output = output.split('_')[0]
        
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()

    @weight(0.2)
    def test_case41(self):
        # Title used by Gradescope 
        """Test Case 41: Tests rename_people()"""

        # Create a subprocess to run the students code with the Third Command Line Option
        test = subprocess.Popen(["./test.out", "9"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "2_1_1"
        message = "Please note that we are only checking for the sum in this test case which we will extract from your answer. Thus, if you have the same sum as the expected answer, the autograder should have marked this as correct even if the rest of the answer differs from the expected answer. We're printing the sequence from both the expected and your answer so you can compare them and use it if needs be (but the sequence is not necessarily unique).\nWe expected this:\n" + expected + "\nWe got this:\n" + output

        expected = expected.split('_')[0]
        output = output.split('_')[0]
        
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()

    @weight(0.2)
    def test_case42(self):
        # Title used by Gradescope 
        """Test Case 42: Tests rename_people()"""

        # Create a subprocess to run the students code with the Third Command Line Option
        test = subprocess.Popen(["./test.out", "9"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "9_1_5_2_6_3_1_4_2_5_3_6_4_7_7_8_9_9_8_10_10"
        message = "Please note that we are only checking for the sum in this test case which we will extract from your answer. Thus, if you have the same sum as the expected answer, the autograder should have marked this as correct even if the rest of the answer differs from the expected answer. We're printing the sequence from both the expected and your answer so you can compare them and use it if needs be (but the sequence is not necessarily unique).\nWe expected this:\n" + expected + "\nWe got this:\n" + output

        expected = expected.split('_')[0]
        output = output.split('_')[0]
        
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()

    @weight(0.2)
    def test_case43(self):
        # Title used by Gradescope 
        """Test Case 43: Tests rename_people()"""

        # Create a subprocess to run the students code with the Third Command Line Option
        test = subprocess.Popen(["./test.out", "9"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "6_1_2_2_6_3_3_4_5_5_10_6_1_7_4_8_7_9_8_10_9"
        message = "Please note that we are only checking for the sum in this test case which we will extract from your answer. Thus, if you have the same sum as the expected answer, the autograder should have marked this as correct even if the rest of the answer differs from the expected answer. We're printing the sequence from both the expected and your answer so you can compare them and use it if needs be (but the sequence is not necessarily unique).\nWe expected this:\n" + expected + "\nWe got this:\n" + output

        expected = expected.split('_')[0]
        output = output.split('_')[0]
        
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()

    @weight(0.2)
    def test_case44(self):
        # Title used by Gradescope 
        """Test Case 44: Tests rename_people()"""

        # Create a subprocess to run the students code with the Third Command Line Option
        test = subprocess.Popen(["./test.out", "9"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "0_1_10_2_9_3_3_4_8_5_1_6_7_7_2_8_4_9_5_10_6"
        message = "Please note that we are only checking for the sum in this test case which we will extract from your answer. Thus, if you have the same sum as the expected answer, the autograder should have marked this as correct even if the rest of the answer differs from the expected answer. We're printing the sequence from both the expected and your answer so you can compare them and use it if needs be (but the sequence is not necessarily unique).\nWe expected this:\n" + expected + "\nWe got this:\n" + output

        expected = expected.split('_')[0]
        output = output.split('_')[0]
        
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()

    @weight(0.2)
    def test_case45(self):
        # Title used by Gradescope 
        """Test Case 45: Tests rename_people()"""

        # Create a subprocess to run the students code with the Third Command Line Option
        test = subprocess.Popen(["./test.out", "9"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "51_1_30_2_10_3_17_4_20_5_26_6_9_7_15_8_22_9_8_10_21_11_7_12_13_13_6_14_24_15_18_16_12_17_29_18_11_19_3_20_2_21_1_22_16_23_27_24_14_25_25_26_19_27_5_28_23_29_4_30_28"
        message = "Please note that we are only checking for the sum in this test case which we will extract from your answer. Thus, if you have the same sum as the expected answer, the autograder should have marked this as correct even if the rest of the answer differs from the expected answer. We're printing the sequence from both the expected and your answer so you can compare them and use it if needs be (but the sequence is not necessarily unique).\nWe expected this:\n" + expected + "\nWe got this:\n" + output

        expected = expected.split('_')[0]
        output = output.split('_')[0]
        
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()

    @weight(0.2)
    def test_case46(self):
        # Title used by Gradescope 
        """Test Case 46: Tests rename_people()"""

        # Create a subprocess to run the students code with the Third Command Line Option
        test = subprocess.Popen(["./test.out", "9"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "51_1_3_2_1_3_2_4_8_5_11_6_4_7_5_8_6_9_10_10_12_11_13_12_14_13_15_14_16_15_19_16_20_17_7_18_9_19_27_20_29_21_32_22_21_23_35_24_22_25_17_26_23_27_24_28_38_29_18_30_36_31_25_32_37_33_26_34_28_35_39_36_30_37_31_38_44_39_33_40_34_41_42_42_45_43_46_44_40_45_41_46_43_47_51_48_48_49_49_50_50_51_47"
        message = "Please note that we are only checking for the sum in this test case which we will extract from your answer. Thus, if you have the same sum as the expected answer, the autograder should have marked this as correct even if the rest of the answer differs from the expected answer. We're printing the sequence from both the expected and your answer so you can compare them and use it if needs be (but the sequence is not necessarily unique).\nWe expected this:\n" + expected + "\nWe got this:\n" + output

        expected = expected.split('_')[0]
        output = output.split('_')[0]
        
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()

    @weight(0.2)
    def test_case47(self):
        # Title used by Gradescope 
        """Test Case 47: Tests rename_people()"""

        # Create a subprocess to run the students code with the Third Command Line Option
        test = subprocess.Popen(["./test.out", "9"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "6_1_8_2_6_3_1_4_3_5_2_6_7_7_5_8_4_9_9_10_10"
        message = "Please note that we are only checking for the sum in this test case which we will extract from your answer. Thus, if you have the same sum as the expected answer, the autograder should have marked this as correct even if the rest of the answer differs from the expected answer. We're printing the sequence from both the expected and your answer so you can compare them and use it if needs be (but the sequence is not necessarily unique).\nWe expected this:\n" + expected + "\nWe got this:\n" + output

        expected = expected.split('_')[0]
        output = output.split('_')[0]
        
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()

    @weight(0.2)
    def test_case48(self):
        # Title used by Gradescope 
        """Test Case 48: Tests rename_people()"""

        # Create a subprocess to run the students code with the Third Command Line Option
        test = subprocess.Popen(["./test.out", "9"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "13_1_1_2_2_3_5_4_4_5_3"
        message = "Please note that we are only checking for the sum in this test case which we will extract from your answer. Thus, if you have the same sum as the expected answer, the autograder should have marked this as correct even if the rest of the answer differs from the expected answer. We're printing the sequence from both the expected and your answer so you can compare them and use it if needs be (but the sequence is not necessarily unique).\nWe expected this:\n" + expected + "\nWe got this:\n" + output

        expected = expected.split('_')[0]
        output = output.split('_')[0]
        
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()

    @weight(0.2)
    def test_case49(self):
        # Title used by Gradescope 
        """Test Case 49: Tests rename_people()"""

        # Create a subprocess to run the students code with the Third Command Line Option
        test = subprocess.Popen(["./test.out", "9"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "9_1_1_2_5_3_7_4_6_5_8_6_2_7_3_8_4"
        message = "Please note that we are only checking for the sum in this test case which we will extract from your answer. Thus, if you have the same sum as the expected answer, the autograder should have marked this as correct even if the rest of the answer differs from the expected answer. We're printing the sequence from both the expected and your answer so you can compare them and use it if needs be (but the sequence is not necessarily unique).\nWe expected this:\n" + expected + "\nWe got this:\n" + output

        expected = expected.split('_')[0]
        output = output.split('_')[0]
        
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()

    @weight(0.2)
    def test_case50(self):
        # Title used by Gradescope 
        """Test Case 50: Tests rename_people()"""

        # Create a subprocess to run the students code with the Third Command Line Option
        test = subprocess.Popen(["./test.out", "9"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "12_1_6_2_1_3_3_4_5_5_2_6_4"
        message = "Please note that we are only checking for the sum in this test case which we will extract from your answer. Thus, if you have the same sum as the expected answer, the autograder should have marked this as correct even if the rest of the answer differs from the expected answer. We're printing the sequence from both the expected and your answer so you can compare them and use it if needs be (but the sequence is not necessarily unique).\nWe expected this:\n" + expected + "\nWe got this:\n" + output

        expected = expected.split('_')[0]
        output = output.split('_')[0]
        
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()

    @weight(0.2)
    def test_case51(self):
        # Title used by Gradescope 
        """Test Case 51: Tests rename_people()"""

        # Create a subprocess to run the students code with the Third Command Line Option
        test = subprocess.Popen(["./test.out", "9"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "61_1_1_2_2"
        message = "Please note that we are only checking for the sum in this test case which we will extract from your answer. Thus, if you have the same sum as the expected answer, the autograder should have marked this as correct even if the rest of the answer differs from the expected answer. We're printing the sequence from both the expected and your answer so you can compare them and use it if needs be (but the sequence is not necessarily unique).\nWe expected this:\n" + expected + "\nWe got this:\n" + output

        expected = expected.split('_')[0]
        output = output.split('_')[0]
        
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()

    @weight(0.2)
    def test_case52(self):
        # Title used by Gradescope 
        """Test Case 52: Tests rename_people()"""

        # Create a subprocess to run the students code with the Third Command Line Option
        test = subprocess.Popen(["./test.out", "9"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "3_1_8_2_2_3_9_4_12_5_1_6_5_7_7_8_4_9_6_10_10_11_3_12_13_13_11"
        message = "Please note that we are only checking for the sum in this test case which we will extract from your answer. Thus, if you have the same sum as the expected answer, the autograder should have marked this as correct even if the rest of the answer differs from the expected answer. We're printing the sequence from both the expected and your answer so you can compare them and use it if needs be (but the sequence is not necessarily unique).\nWe expected this:\n" + expected + "\nWe got this:\n" + output

        expected = expected.split('_')[0]
        output = output.split('_')[0]
        
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()

    @weight(0.2)
    def test_case53(self):
        # Title used by Gradescope 
        """Test Case 53: Tests rename_people()"""

        # Create a subprocess to run the students code with the Third Command Line Option
        test = subprocess.Popen(["./test.out", "9"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "0"
        message = "Please note that we are only checking for the sum in this test case which we will extract from your answer. Thus, if you have the same sum as the expected answer, the autograder should have marked this as correct even if the rest of the answer differs from the expected answer. We're printing the sequence from both the expected and your answer so you can compare them and use it if needs be (but the sequence is not necessarily unique).\nWe expected this:\n" + expected + "\nWe got this:\n" + output

        expected = expected.split('_')[0]
        output = output.split('_')[0]
        
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()

    @weight(0.2)
    def test_case54(self):
        # Title used by Gradescope 
        """Test Case 54: Tests rename_people()"""

        # Create a subprocess to run the students code with the Third Command Line Option
        test = subprocess.Popen(["./test.out", "9"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "0_1_1"
        message = "Please note that we are only checking for the sum in this test case which we will extract from your answer. Thus, if you have the same sum as the expected answer, the autograder should have marked this as correct even if the rest of the answer differs from the expected answer. We're printing the sequence from both the expected and your answer so you can compare them and use it if needs be (but the sequence is not necessarily unique).\nWe expected this:\n" + expected + "\nWe got this:\n" + output

        expected = expected.split('_')[0]
        output = output.split('_')[0]
        
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()

    @weight(0.2)
    def test_case55(self):
        # Title used by Gradescope 
        """Test Case 55: Tests rename_people()"""

        # Create a subprocess to run the students code with the Third Command Line Option
        test = subprocess.Popen(["./test.out", "9"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "5_1_1"
        message = "Please note that we are only checking for the sum in this test case which we will extract from your answer. Thus, if you have the same sum as the expected answer, the autograder should have marked this as correct even if the rest of the answer differs from the expected answer. We're printing the sequence from both the expected and your answer so you can compare them and use it if needs be (but the sequence is not necessarily unique).\nWe expected this:\n" + expected + "\nWe got this:\n" + output

        expected = expected.split('_')[0]
        output = output.split('_')[0]
        
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()

    @weight(0.2)
    def test_case56(self):
        # Title used by Gradescope 
        """Test Case 56: Tests rename_people()"""

        # Create a subprocess to run the students code with the Third Command Line Option
        test = subprocess.Popen(["./test.out", "9"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "0_1_1"
        message = "Please note that we are only checking for the sum in this test case which we will extract from your answer. Thus, if you have the same sum as the expected answer, the autograder should have marked this as correct even if the rest of the answer differs from the expected answer. We're printing the sequence from both the expected and your answer so you can compare them and use it if needs be (but the sequence is not necessarily unique).\nWe expected this:\n" + expected + "\nWe got this:\n" + output

        expected = expected.split('_')[0]
        output = output.split('_')[0]
        
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()

    @weight(0.2)
    def test_case57(self):
        # Title used by Gradescope 
        """Test Case 57: Tests rename_people()"""

        # Create a subprocess to run the students code with the Third Command Line Option
        test = subprocess.Popen(["./test.out", "9"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "0_1_1"
        message = "Please note that we are only checking for the sum in this test case which we will extract from your answer. Thus, if you have the same sum as the expected answer, the autograder should have marked this as correct even if the rest of the answer differs from the expected answer. We're printing the sequence from both the expected and your answer so you can compare them and use it if needs be (but the sequence is not necessarily unique).\nWe expected this:\n" + expected + "\nWe got this:\n" + output

        expected = expected.split('_')[0]
        output = output.split('_')[0]
        
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()

    @weight(0.2)
    def test_case58(self):
        # Title used by Gradescope 
        """Test Case 58: Tests rename_people()"""

        # Create a subprocess to run the students code with the Third Command Line Option
        test = subprocess.Popen(["./test.out", "9"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "1_1_1"
        message = "Please note that we are only checking for the sum in this test case which we will extract from your answer. Thus, if you have the same sum as the expected answer, the autograder should have marked this as correct even if the rest of the answer differs from the expected answer. We're printing the sequence from both the expected and your answer so you can compare them and use it if needs be (but the sequence is not necessarily unique).\nWe expected this:\n" + expected + "\nWe got this:\n" + output

        expected = expected.split('_')[0]
        output = output.split('_')[0]
        
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()

    @weight(0.2)
    def test_case59(self):
        # Title used by Gradescope 
        """Test Case 59: Tests rename_people()"""

        # Create a subprocess to run the students code with the Third Command Line Option
        test = subprocess.Popen(["./test.out", "9"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "4_1_2_2_1_3_3"
        message = "Please note that we are only checking for the sum in this test case which we will extract from your answer. Thus, if you have the same sum as the expected answer, the autograder should have marked this as correct even if the rest of the answer differs from the expected answer. We're printing the sequence from both the expected and your answer so you can compare them and use it if needs be (but the sequence is not necessarily unique).\nWe expected this:\n" + expected + "\nWe got this:\n" + output

        expected = expected.split('_')[0]
        output = output.split('_')[0]
        
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()

    @weight(0.2)
    def test_case60(self):
        # Title used by Gradescope 
        """Test Case 60: Tests rename_people()"""

        # Create a subprocess to run the students code with the Third Command Line Option
        test = subprocess.Popen(["./test.out", "9"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "11_1_1_2_2_3_3_4_4"
        message = "Please note that we are only checking for the sum in this test case which we will extract from your answer. Thus, if you have the same sum as the expected answer, the autograder should have marked this as correct even if the rest of the answer differs from the expected answer. We're printing the sequence from both the expected and your answer so you can compare them and use it if needs be (but the sequence is not necessarily unique).\nWe expected this:\n" + expected + "\nWe got this:\n" + output

        expected = expected.split('_')[0]
        output = output.split('_')[0]
        
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()

    @weight(0.25)
    def test_case61(self):
        # Title used by Gradescope 
        """Test Case 61: Tests rename_people()"""

        # Create a subprocess to run the students code with the Third Command Line Option
        test = subprocess.Popen(["./test.out", "9"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "17_1_8_2_10_3_5_4_7_5_6_6_4_7_2_8_9_9_3_10_1"
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output

        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()

    @weight(0.25)
    def test_case62(self):
        # Title used by Gradescope 
        """Test Case 62: Tests rename_people()"""

        # Create a subprocess to run the students code with the Third Command Line Option
        test = subprocess.Popen(["./test.out", "9"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stdout.read().strip().decode('utf-8')
        test.kill()

        expected = "11_1_3_2_5_3_4_4_1_5_2"
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output

        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
        test.terminate()


    runTime = time.time() - start_time

  

   