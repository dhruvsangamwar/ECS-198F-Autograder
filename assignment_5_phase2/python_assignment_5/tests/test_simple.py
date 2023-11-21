import unittest
import time
import collections
from gradescope_utils.autograder_utils.decorators import weight, number, visibility

from homework5 import count_scores
from homework5 import rename_people

runTime = 0.0

class TestDiff(unittest.TestCase):
    global runTime
    start_time = time.time()

    # Associated point value within GradeScope
    @weight(0)
    def test_Compile(self):
        #Title used by Gradescope 
        """Clean Compile"""

        expected = ""
        output = ""
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output

        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)

    # Associated point value within GradeScope
    @weight(0)
    def test_case0(self):
        #Title used by Gradescope 
        """Test Case 0 - Making sure Autograder works"""


        expected = "Gradescope working properly - should be always correct, please ignore"
        output = "Gradescope working properly - should be always correct, please ignore"
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output

        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)

    @weight(0.1)
    def test_case1(self):
        #Title used by Gradescope 
        """Test Case 1: Tests count_scores()"""

        expected = "YES_NO_NO"
        output = count_scores(2, 3, "aaaaa_acacaca", "aabaa_ccacacc_caaac")
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output

        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)

    @weight(0.1)
    def test_case2(self):
        #Title used by Gradescope 
        """Test Case 2: Tests count_scores()"""

        expected = "NO_NO_NO_NO_YES"
        output = count_scores(1, 5, "acbacbacb", "cbacbacb_acbacbac_aacbacbacb_acbacbacbb_acbaabacb")
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output

        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)

    @weight(0.1)
    def test_case3(self):
        #Title used by Gradescope 
        """Test Case 3: Tests count_scores()"""

        expected = ""
        output = count_scores(0, 0, "", "")
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output

        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)

    @weight(0.1)
    def test_case4(self):
        #Title used by Gradescope 
        """Test Case 4: Tests count_scores()"""

        expected = "YES_YES_NO_YES"
        output = count_scores(5, 4, "ab_cacab_cbabc_acc_cacab", "abc_aa_acbca_cb")
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output

        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)

    @weight(0.1)
    def test_case5(self):
        #Title used by Gradescope 
        """Test Case 5: Tests count_scores()"""

        expected = "YES_NO_NO_NO_NO_NO_YES_YES_NO"
        output = count_scores(9, 9, "caccbcacabccba_aacbcbcaabacbcbcba_babccaaacccacbb_caaabcaacbababbabbb_abbaccacabacaaaa_bccbccababcaacb_caacbcaacbababbabbb_bcacababbbcaaca_ccbbcbababbccaab", "bbcbccababcaacb_aacccbabbacbabacaca_bbcbcccbabcaacb_acbacacbcacc_caaabcaaabacabbabbb_abbbabaaaba_aacccbcaabacbcbcba_abbaccacabbcaaaa_aaccbbcabbacbcbcba")
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output

        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)

    @weight(0.1)
    def test_case6(self):
        #Title used by Gradescope 
        """Test Case 6: Tests count_scores()"""

        expected = "NO_NO_NO_NO_NO_NO_NO_NO_NO"
        output = count_scores(0, 9, "", "caccbcacabccba_aacbcbcaabacbcbcba_babccaaacccacbb_caaabcaacbababbabbb_abbaccacabacaaaa_bccbccababcaacb_caacbcaacbababbabbb_bcacababbbcaaca_ccbbcbababbccaab")
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output

        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)

    @weight(0.1)
    def test_case7(self):
        #Title used by Gradescope 
        """Test Case 7: Tests count_scores()"""

        expected = ""
        output = count_scores(9, 0, "caccbcacabccba_aacbcbcaabacbcbcba_babccaaacccacbb_caaabcaacbababbabbb_abbaccacabacaaaa_bccbccababcaacb_caacbcaacbababbabbb_bcacababbbcaaca_ccbbcbababbccaab", "")
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output

        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)

    @weight(0.1)
    def test_case8(self):
        #Title used by Gradescope 
        """Test Case 8: Tests count_scores()"""

        expected = "NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO_NO"
        output = count_scores(200, 200, "bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac", "bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac")
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output

        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)

    @weight(0.1)
    def test_case9(self):
        #Title used by Gradescope 
        """Test Case 9: Tests count_scores()"""

        expected = "YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES"
        output = count_scores(200, 200, "bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac_bcabbaacac", "bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc_bcabbaacdc")
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output

        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)

    @weight(0.1)
    def test_case10(self):
        #Title used by Gradescope 
        """Test Case 10: Tests count_scores()"""

        expected = "YES_YES_YES"
        output = count_scores(2, 3, "a_c", "b_c_a")
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output

        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)

    @weight(0.1)
    def test_case11(self):
        #Title used by Gradescope 
        """Test Case 11: Tests count_scores()11: Tests count_scores()"""

        expected = "YES_NO"
        output = count_scores(3, 2, "a_b_c", "a_bb")
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output

        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)

    @weight(0.1)
    def test_case12(self):
        #Title used by Gradescope 
        """Test Case 12: Tests count_scores()"""

        expected = "YES_YES_YES_YES"
        output = count_scores(3, 4, "aa_bb", "ac_cb_ab_ba")
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output

        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)

    @weight(0.1)
    def test_case13(self):
        #Title used by Gradescope 
        """Test Case 13: Tests count_scores()"""

        expected = "YES_NO"
        output = count_scores(2, 3, "aabc_ca", "aacc_bb")
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output

        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)

    @weight(0.1)
    def test_case14(self):
        #Title used by Gradescope 
        """Test Case 14: Tests count_scores()"""

        expected = "YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_YES_NO"
        output = count_scores(14, 14, "abc_bca_cab_aab_aba_baa_aca_caa_bcc_aaa_bbb_ccc_abb_abbcb", "abc_bca_cab_aab_aba_baa_aca_caa_bcc_aaa_bbb_ccc_abb_abbcb")
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output

        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)


    @weight(0.1)
    def test_case15(self):
        #Title used by Gradescope 
        """Test Case 15: Tests count_scores()"""

        expected = "YES"
        output = count_scores(1, 1, "ccaaaabacbbaaacbcaccbaabaabcaacbbbaabcabbbcabcbbacccabaabcbbcbbbbbbcbacaaabcccacaacbbbbaaccabcbcaaacbabbbbcaabaaabaabaabaccbbcaacccabcacaaabacccccaacbbccbcbcbccaacbabbccbccabbcabacbacccbaababacabababbaabaabccccbcbaabababbccbcaacaacaaabbaccababcabacaaccbbbacbccacacbbbacccccbabcbaacbabaabcabaacbcaacacacbabcacbabaabbcccaccacbccbacccacbbaacaaacaacabcacccccaaaccbcbbcaaabbcbcbacabcaccabbabccccaccccabbababbccacccaacccacbbacbccbbacccbcbbcbacaaacaacbbaabacacacaabcaacbbbbacbccccccbbacaabaccacbaccccaacacbcacbbab", "ccaaaabacbbaaacbcaccbaabaabcaacbbbaabcabbbcabcbbacccabaabcbbcbbbbbbcbacaaabcccacaacbbbbaaccabcbcaaacbabbbbcaabaaabaabaabaccbbcaacccabcacaaabacccccaacbbccbcbcbccaacbabbccbccabbcabacbacccbaababacabababbaabaabccccbcbaabababbccbcaacaacaaabbaccababcabacaaccbbbacbccacacbbbacccccbabcbaacbabaabcabaacbcaacacacbabcacbabaabbcccaccacbccbacccacbbaacaaacaacabcacccccaaaccbcbbcaaabbcbcbacabcaccabbabccccaccccabbababbccacccaacccacbbacbccbbacccbcbbcbacaaacaacbbaabacacacaabcaacbbbbacbccccccbbacaabaccacbaccccaacacbcacbbac")
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output

        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)

    @weight(0.1)
    def test_case16(self):
        #Title used by Gradescope 
        """Test Case 16: Tests count_scores()"""

        expected = "NO_NO_YES_YES_YES_YES_YES_YES_YES_YES"
        output = count_scores(1, 10, "ab", "cc_abc_aa_aa_aa_aa_aa_aa_aa_aa")
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output

        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)

    @weight(0.1)
    def test_case17(self):
        #Title used by Gradescope 
        """Test Case 17: Tests count_scores()"""

        expected = "YES"
        output = count_scores(10, 1, "cc_abc_aa_aa_aa_aa_aa_aa_aa_aa", "ab")
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output

        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)

    @weight(0.1)
    def test_case18(self):
        #Title used by Gradescope 
        """Test Case 18: Tests count_scores()"""

        expected = "NO"
        output = count_scores(1, 1, "c", "ccccccccccc")
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output

        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)

    @weight(0.1)
    def test_case19(self):
        #Title used by Gradescope 
        """Test Case 19: Tests count_scores()"""

        expected = "NO"
        output = count_scores(1, 1, "bbbbbbbaaaabbbbbaabbbba", "aaabbbabbbbbbbaabbabbbb")
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output

        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)

    @weight(0.1)
    def test_case20(self):
        #Title used by Gradescope 
        """Test Case 20: Tests count_scores()"""

        expected = "YES"
        output = count_scores(1, 1, "bbbbbbbaaaabbbbbaabbbba", "bbbbbbbaaaabbbbbaabbbbb")
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output

        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)

    @weight(0.1)
    def test_case21(self):
        #Title used by Gradescope 
        """Test Case 21: Tests count_scores()"""

        expected = "NO_NO_NO"
        output = count_scores(3, 3, "abc_abb_a", "ab_ab_ab")
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output

        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)

    @weight(0.1)
    def test_case22(self):
        #Title used by Gradescope 
        """Test Case 22: Tests count_scores()"""

        expected = "YES_YES_NO_NO_NO_YES_YES_NO_NO_NO_YES_YES_NO_NO_NO_YES_YES_NO_NO_NO"
        output = count_scores(10, 20, "a_b_c_bb_aa_cc_abc_bac_ccc_acc", "ca_bbc_aaa_bbb_caa_baa_acb_aaa_bbb_caa_ca_bbc_aaa_bbb_caa_baa_acb_aaa_bbb_caa")
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output

        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)

    @weight(0.1)
    def test_case23(self):
        #Title used by Gradescope 
        """Test Case 23: Tests count_scores()"""

        expected = "NO_NO_YES_YES_YES_NO"
        output = count_scores(1, 6, "aaaaaaaaaaaaa", "aaaaaaaaaaaaa_bbbbbbbbbbbbb_caaaaaaaaaaaa_aaaaaaaaaaaac_aaaaaaabaaaaa_baaaaaaaaaaca")
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output

        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)

    @weight(0.1)
    def test_case24(self):
        #Title used by Gradescope 
        """Test Case 24: Tests count_scores()"""

        expected = "NO_YES_NO_NO"
        output = count_scores(2, 4, "abc_acb", "acb_aba_aaa_ac")
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output

        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)

    @weight(0.1)
    def test_case25(self):
        #Title used by Gradescope 
        """Test Case 25: Tests count_scores()"""

        expected = "NO_YES_NO_YES_NO_YES_YES_YES_YES_YES"
        output = count_scores(2, 2, "ab_bc", "ab_aa_ab_ac_bc_ba_bb_aa_cc_ac")
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output

        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)

    @weight(0.2)
    def test_case26(self):
        #Title used by Gradescope 
        """Test Case 26: Tests count_scores()"""

        expected = "79_1_1"
        output = rename_people(1, "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        message = "Please note that we are only checking for the sum in this test case which we will extract from your answer. Thus, if you have the same sum as the expected answer, the autograder should have marked this as correct even if the rest of the answer differs from the expected answer. We're printing the sequence from both the expected and your answer so you can compare them and use it if needs be (but the sequence is not necessarily unique).\nWe expected this:\n" + expected + "\nWe got this:\n" + output

        expected = expected.split('_')[0]
        output = output.split('_')[0]

        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
    
    # Associated point value within GradeScope
    @weight(0.2)
    def test_case27(self):
        # Title used by Gradescope 
        """Test Case 27: Tests count_scores()"""

        expected = "6_1_2_2_1"
        output = rename_people(2, "aaaa_aaa", "aa_aaaa")
        message = "Please note that we are only checking for the sum in this test case which we will extract from your answer. Thus, if you have the same sum as the expected answer, the autograder should have marked this as correct even if the rest of the answer differs from the expected answer. We're printing the sequence from both the expected and your answer so you can compare them and use it if needs be (but the sequence is not necessarily unique).\nWe expected this:\n" + expected + "\nWe got this:\n" + output

        expected = expected.split('_')[0]
        output = output.split('_')[0]
        
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)

    # Associated point value within GradeScope
    @weight(0.2)
    def test_case28(self):
        # Title used by Gradescope 
        """Test Case 28: Tests count_scores()"""

        expected = "7_1_3_2_1_3_2_4_4"
        output = rename_people(4, 4, "aaa_bba_ccb_dcss", "bba_ccb_acc_caa")
        message = "Please note that we are only checking for the sum in this test case which we will extract from your answer. Thus, if you have the same sum as the expected answer, the autograder should have marked this as correct even if the rest of the answer differs from the expected answer. We're printing the sequence from both the expected and your answer so you can compare them and use it if needs be (but the sequence is not necessarily unique).\nWe expected this:\n" + expected + "\nWe got this:\n" + output

        expected = expected.split('_')[0]
        output = output.split('_')[0]
        
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
    
    @weight(0.2)
    def test_case29(self):
        # Title used by Gradescope 
        """Test Case 29: Tests count_scores()"""

        expected = "8_1_3_2_6_3_5_4_7_5_4_6_1_7_2"
        output = rename_people(7, "a_cc_aaa_bb_bca_acb_aa", "aba_aac_hhd_bcd_aad_ooa_bab")
        message = "Please note that we are only checking for the sum in this test case which we will extract from your answer. Thus, if you have the same sum as the expected answer, the autograder should have marked this as correct even if the rest of the answer differs from the expected answer. We're printing the sequence from both the expected and your answer so you can compare them and use it if needs be (but the sequence is not necessarily unique).\nWe expected this:\n" + expected + "\nWe got this:\n" + output

        expected = expected.split('_')[0]
        output = output.split('_')[0]
        
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
    
    @weight(0.2)
    def test_case30(self):
        # Title used by Gradescope 
        """Test Case 30: Tests count_scores()"""

        expected = "501_1_1"
        output = rename_people(1, "baababbaabbabaababbabaabbaababbaabbabaabbaababbabaababbaabbabaababbabaabbaababbabaababbaabbabaabbaababbaabbabaababbabaabbaababbaabbabaabbaababbabaababbaabbabaabbaababbaabbabaababbabaabbaababbabaababbaabbabaababbabaabbaababbaabbabaabbaababbabaababbaabbabaababbabaabbaababbabaababbaabbabaabbaababbaabbabaababbabaabbaababbabaababbaabbabaababbabaabbaababbaabbabaabbaababbabaababbaabbabaabbaababbaabbabaababbabaabbaababbaabbabaabbaababbabaababbaabbabaababbabaabbaababbabaababbaabbabaabbaababbaabbabaababbabaabba", "baababbaabbabaababbabaabbaababbaabbabaabbaababbabaababbaabbabaababbabaabbaababbabaababbaabbabaabbaababbaabbabaababbabaabbaababbaabbabaabbaababbabaababbaabbabaabbaababbaabbabaababbabaabbaababbabaababbaabbabaababbabaabbaababbaabbabaabbaababbabaababbaabbabaababbabaabbaababbabaababbaabbabaabbaababbaabbabaababbabaabbaababbabaababbaabbabaababbabaabbaababbaabbabaabbaababbabaababbaabbabaabbaababbaabbabaababbabaabbaababbaabbabaabbaababbabaababbaabbabaababbabaabbaababbabaababbaabbabaabbaababbaabbabaababbabcabba")
        message = "Please note that we are only checking for the sum in this test case which we will extract from your answer. Thus, if you have the same sum as the expected answer, the autograder should have marked this as correct even if the rest of the answer differs from the expected answer. We're printing the sequence from both the expected and your answer so you can compare them and use it if needs be (but the sequence is not necessarily unique).\nWe expected this:\n" + expected + "\nWe got this:\n" + output

        expected = expected.split('_')[0]
        output = output.split('_')[0]
        
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)
    
    @weight(0.2)
    def test_case31(self):
        # Title used by Gradescope 
        """Test Case 31: Tests rename_people()"""

        expected = "9_1_3_2_2_3_1_4_4_5_5"
        output = rename_people(5, "geeennady_galya_bdris_bal_toshik", "bbbilbo_torin_geneealf_smaug_toshikaaadnjn")
        message = "Please note that we are only checking for the sum in this test case which we will extract from your answer. Thus, if you have the same sum as the expected answer, the autograder should have marked this as correct even if the rest of the answer differs from the expected answer. We're printing the sequence from both the expected and your answer so you can compare them and use it if needs be (but the sequence is not necessarily unique).\nWe expected this:\n" + expected + "\nWe got this:\n" + output

        expected = expected.split('_')[0]
        output = output.split('_')[0]
        
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)

    @weight(0.2)
    def test_case32(self):
        # Title used by Gradescope 
        """Test Case 32: Tests rename_people()"""

        expected = "1_1_1"
        output = rename_people(1, "a", "a")
        message = "Please note that we are only checking for the sum in this test case which we will extract from your answer. Thus, if you have the same sum as the expected answer, the autograder should have marked this as correct even if the rest of the answer differs from the expected answer. We're printing the sequence from both the expected and your answer so you can compare them and use it if needs be (but the sequence is not necessarily unique).\nWe expected this:\n" + expected + "\nWe got this:\n" + output

        expected = expected.split('_')[0]
        output = output.split('_')[0]
        
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)

    @weight(0.2)
    def test_case33(self):
        # Title used by Gradescope 
        """Test Case 33: Tests rename_people()"""

        expected = "2_1_1_2_2"
        output = rename_people(2, "a_a", "a_a")
        message = "Please note that we are only checking for the sum in this test case which we will extract from your answer. Thus, if you have the same sum as the expected answer, the autograder should have marked this as correct even if the rest of the answer differs from the expected answer. We're printing the sequence from both the expected and your answer so you can compare them and use it if needs be (but the sequence is not necessarily unique).\nWe expected this:\n" + expected + "\nWe got this:\n" + output

        expected = expected.split('_')[0]
        output = output.split('_')[0]
        
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)

    @weight(0.2)
    def test_case34(self):
        # Title used by Gradescope 
        """Test Case 34: Tests rename_people()"""

        expected = "1_1_2_2_1"
        output = rename_people(2, "a_b", "a_a")
        message = "Please note that we are only checking for the sum in this test case which we will extract from your answer. Thus, if you have the same sum as the expected answer, the autograder should have marked this as correct even if the rest of the answer differs from the expected answer. We're printing the sequence from both the expected and your answer so you can compare them and use it if needs be (but the sequence is not necessarily unique).\nWe expected this:\n" + expected + "\nWe got this:\n" + output

        expected = expected.split('_')[0]
        output = output.split('_')[0]
        
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)

    @weight(0.2)
    def test_case35(self):
        # Title used by Gradescope 
        """Test Case 35: Tests rename_people()"""

        expected = "0_1_1_2_2"
        output = rename_people(2, "b_b", "a_a")
        message = "Please note that we are only checking for the sum in this test case which we will extract from your answer. Thus, if you have the same sum as the expected answer, the autograder should have marked this as correct even if the rest of the answer differs from the expected answer. We're printing the sequence from both the expected and your answer so you can compare them and use it if needs be (but the sequence is not necessarily unique).\nWe expected this:\n" + expected + "\nWe got this:\n" + output

        expected = expected.split('_')[0]
        output = output.split('_')[0]
        
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)


    @weight(0.2)
    def test_case36(self):
        # Title used by Gradescope 
        """Test Case 36: Tests rename_people()"""

        expected = "2_1_1_2_2"
        output = rename_people(2, "a_b", "a_b")
        message = "Please note that we are only checking for the sum in this test case which we will extract from your answer. Thus, if you have the same sum as the expected answer, the autograder should have marked this as correct even if the rest of the answer differs from the expected answer. We're printing the sequence from both the expected and your answer so you can compare them and use it if needs be (but the sequence is not necessarily unique).\nWe expected this:\n" + expected + "\nWe got this:\n" + output

        expected = expected.split('_')[0]
        output = output.split('_')[0]
        
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)

    @weight(0.2)
    def test_case37(self):
        # Title used by Gradescope 
        """Test Case 37: Tests rename_people()"""

        expected = "3_1_1_2_3_3_2"
        output = rename_people(3, "a_b_c", "a_c_b")
        message = "Please note that we are only checking for the sum in this test case which we will extract from your answer. Thus, if you have the same sum as the expected answer, the autograder should have marked this as correct even if the rest of the answer differs from the expected answer. We're printing the sequence from both the expected and your answer so you can compare them and use it if needs be (but the sequence is not necessarily unique).\nWe expected this:\n" + expected + "\nWe got this:\n" + output

        expected = expected.split('_')[0]
        output = output.split('_')[0]
        
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)

    @weight(0.2)
    def test_case38(self):
        # Title used by Gradescope 
        """Test Case 38: Tests rename_people()"""

        expected = "10_1_8_2_5_3_10_4_1_5_3_6_7_7_6_8_9_9_4_10_2"
        output = rename_people(10, "abaabbaaa_acccccaacabc_acbaabaaabbca_aaccca_cbbba_aaba_acab_ac_cbac_ca", "bbbbc_bacbcbcaac_c_cba_a_abba_bcabc_abcccaa_ab_a")
        message = "Please note that we are only checking for the sum in this test case which we will extract from your answer. Thus, if you have the same sum as the expected answer, the autograder should have marked this as correct even if the rest of the answer differs from the expected answer. We're printing the sequence from both the expected and your answer so you can compare them and use it if needs be (but the sequence is not necessarily unique).\nWe expected this:\n" + expected + "\nWe got this:\n" + output

        expected = expected.split('_')[0]
        output = output.split('_')[0]
        
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)

    @weight(0.2)
    def test_case39(self):
        # Title used by Gradescope 
        """Test Case 39: Tests rename_people()"""

        expected = "0_1_1"
        output = rename_people(1, "zzzz", "yyx")
        message = "Please note that we are only checking for the sum in this test case which we will extract from your answer. Thus, if you have the same sum as the expected answer, the autograder should have marked this as correct even if the rest of the answer differs from the expected answer. We're printing the sequence from both the expected and your answer so you can compare them and use it if needs be (but the sequence is not necessarily unique).\nWe expected this:\n" + expected + "\nWe got this:\n" + output

        expected = expected.split('_')[0]
        output = output.split('_')[0]
        
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)

    @weight(0.2)
    def test_case40(self):
        # Title used by Gradescope 
        """Test Case 40: Tests rename_people()"""

        expected = "2_1_1"
        output = rename_people(1, "aa", "aaa")
        message = "Please note that we are only checking for the sum in this test case which we will extract from your answer. Thus, if you have the same sum as the expected answer, the autograder should have marked this as correct even if the rest of the answer differs from the expected answer. We're printing the sequence from both the expected and your answer so you can compare them and use it if needs be (but the sequence is not necessarily unique).\nWe expected this:\n" + expected + "\nWe got this:\n" + output

        expected = expected.split('_')[0]
        output = output.split('_')[0]
        
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)

    @weight(0.2)
    def test_case41(self):
        # Title used by Gradescope 
        """Test Case 41: Tests rename_people()"""

        expected = "2_1_1"
        output = rename_people(1, "aaa", "aa")
        message = "Please note that we are only checking for the sum in this test case which we will extract from your answer. Thus, if you have the same sum as the expected answer, the autograder should have marked this as correct even if the rest of the answer differs from the expected answer. We're printing the sequence from both the expected and your answer so you can compare them and use it if needs be (but the sequence is not necessarily unique).\nWe expected this:\n" + expected + "\nWe got this:\n" + output

        expected = expected.split('_')[0]
        output = output.split('_')[0]
        
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)

    @weight(0.2)
    def test_case42(self):
        # Title used by Gradescope 
        """Test Case 42: Tests rename_people()"""

        expected = "9_1_5_2_6_3_1_4_2_5_3_6_4_7_7_8_9_9_8_10_10"
        output = rename_people(10, "b_b_a_a_a_a_b_b_a_b", "b_a_a_a_b_b_b_a_b_b")
        message = "Please note that we are only checking for the sum in this test case which we will extract from your answer. Thus, if you have the same sum as the expected answer, the autograder should have marked this as correct even if the rest of the answer differs from the expected answer. We're printing the sequence from both the expected and your answer so you can compare them and use it if needs be (but the sequence is not necessarily unique).\nWe expected this:\n" + expected + "\nWe got this:\n" + output

        expected = expected.split('_')[0]
        output = output.split('_')[0]
        
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)

    @weight(0.2)
    def test_case43(self):
        # Title used by Gradescope 
        """Test Case 43: Tests rename_people()"""

        expected = "6_1_2_2_6_3_3_4_5_5_10_6_1_7_4_8_7_9_8_10_9"
        output = rename_people(10, "a_b_a_a_c_a_a_a_a_a", "b_c_c_a_c_b_a_a_a_c")
        message = "Please note that we are only checking for the sum in this test case which we will extract from your answer. Thus, if you have the same sum as the expected answer, the autograder should have marked this as correct even if the rest of the answer differs from the expected answer. We're printing the sequence from both the expected and your answer so you can compare them and use it if needs be (but the sequence is not necessarily unique).\nWe expected this:\n" + expected + "\nWe got this:\n" + output

        expected = expected.split('_')[0]
        output = output.split('_')[0]
        
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)

    @weight(0.2)
    def test_case44(self):
        # Title used by Gradescope 
        """Test Case 44: Tests rename_people()"""

        expected = "0_1_10_2_9_3_3_4_8_5_1_6_7_7_2_8_4_9_5_10_6"
        output = rename_people(10, "w_r_a_c_x_e_b_x_w_x", "z_g_d_y_s_y_j_h_l_u")
        message = "Please note that we are only checking for the sum in this test case which we will extract from your answer. Thus, if you have the same sum as the expected answer, the autograder should have marked this as correct even if the rest of the answer differs from the expected answer. We're printing the sequence from both the expected and your answer so you can compare them and use it if needs be (but the sequence is not necessarily unique).\nWe expected this:\n" + expected + "\nWe got this:\n" + output

        expected = expected.split('_')[0]
        output = output.split('_')[0]
        
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)

    @weight(0.2)
    def test_case45(self):
        # Title used by Gradescope 
        """Test Case 45: Tests rename_people()"""

        expected = "51_1_30_2_10_3_17_4_20_5_26_6_9_7_15_8_22_9_8_10_21_11_7_12_13_13_6_14_24_15_18_16_12_17_29_18_11_19_3_20_2_21_1_22_16_23_27_24_14_25_25_26_19_27_5_28_23_29_4_30_28"
        output = rename_people(30, "cb_ac_ac_bb_a_ccbbb_cb_bccaba_bca_a_ccbbbbcac_a_cba_b_aa_cca_bc_ac_acc_babc_caaa_bca_bacaaaaabcacb_c_caa_cb_bac_cc_baa_cc", "caacc_babbcbcbbc_acaa_bb_bbabaacb_cbaaac_cc_bcbccaac_ccc_ab_acaba_ccab_ab_a_c_bcabcab_ac_aaac_cb_bbcbbccb_ab_bccc_cabb_a_cac_abcbc_bb_cab_bc_cacccccc")
        message = "Please note that we are only checking for the sum in this test case which we will extract from your answer. Thus, if you have the same sum as the expected answer, the autograder should have marked this as correct even if the rest of the answer differs from the expected answer. We're printing the sequence from both the expected and your answer so you can compare them and use it if needs be (but the sequence is not necessarily unique).\nWe expected this:\n" + expected + "\nWe got this:\n" + output

        expected = expected.split('_')[0]
        output = output.split('_')[0]
        
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)

    @weight(0.2)
    def test_case46(self):
        # Title used by Gradescope 
        """Test Case 46: Tests rename_people()"""

        expected = "51_1_3_2_1_3_2_4_8_5_11_6_4_7_5_8_6_9_10_10_12_11_13_12_14_13_15_14_16_15_19_16_20_17_7_18_9_19_27_20_29_21_32_22_21_23_35_24_22_25_17_26_23_27_24_28_38_29_18_30_36_31_25_32_37_33_26_34_28_35_39_36_30_37_31_38_44_39_33_40_34_41_42_42_45_43_46_44_40_45_41_46_43_47_51_48_48_49_49_50_50_51_47"
        output = rename_people(51, "a_c_c_c_b_a_a_a_c_c_c_c_c_b_c_c_a_a_a_a_a_c_a_c_b_c_c_c_b_a_b_a_b_b_a_b_b_c_b_b_b_c_c_a_a_a_c_a_a_a_b", "c_c_a_a_a_a_a_c_a_c_b_c_c_c_c_b_b_b_c_c_c_c_c_c_b_b_a_b_a_b_b_a_b_b_a_a_a_c_a_a_a_b_a_c_c_c_b_a_a_a_c")
        message = "Please note that we are only checking for the sum in this test case which we will extract from your answer. Thus, if you have the same sum as the expected answer, the autograder should have marked this as correct even if the rest of the answer differs from the expected answer. We're printing the sequence from both the expected and your answer so you can compare them and use it if needs be (but the sequence is not necessarily unique).\nWe expected this:\n" + expected + "\nWe got this:\n" + output

        expected = expected.split('_')[0]
        output = output.split('_')[0]
        
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)

    @weight(0.2)
    def test_case47(self):
        # Title used by Gradescope 
        """Test Case 47: Tests rename_people()"""

        expected = "6_1_8_2_6_3_1_4_3_5_2_6_7_7_5_8_4_9_9_10_10"
        output = rename_people(10, "we_i_o_d_jt_wh_l_k_v_b", "w_v_c_km_wa_mh_wee_wei_vo_bb")
        message = "Please note that we are only checking for the sum in this test case which we will extract from your answer. Thus, if you have the same sum as the expected answer, the autograder should have marked this as correct even if the rest of the answer differs from the expected answer. We're printing the sequence from both the expected and your answer so you can compare them and use it if needs be (but the sequence is not necessarily unique).\nWe expected this:\n" + expected + "\nWe got this:\n" + output

        expected = expected.split('_')[0]
        output = output.split('_')[0]
        
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)

    @weight(0.2)
    def test_case48(self):
        # Title used by Gradescope 
        """Test Case 48: Tests rename_people()"""

        expected = "13_1_1_2_2_3_5_4_4_5_3"
        output = rename_people(5, "aa_aca_avvs_abb_abca", "aaaa_acxa_abcaa_avas_avvs")
        message = "Please note that we are only checking for the sum in this test case which we will extract from your answer. Thus, if you have the same sum as the expected answer, the autograder should have marked this as correct even if the rest of the answer differs from the expected answer. We're printing the sequence from both the expected and your answer so you can compare them and use it if needs be (but the sequence is not necessarily unique).\nWe expected this:\n" + expected + "\nWe got this:\n" + output

        expected = expected.split('_')[0]
        output = output.split('_')[0]
        
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)

    @weight(0.2)
    def test_case49(self):
        # Title used by Gradescope 
        """Test Case 49: Tests rename_people()"""

        expected = "9_1_1_2_5_3_7_4_6_5_8_6_2_7_3_8_4"
        output = rename_people(8, "aa_acc_abb_aba_bac_bcc_ca_ac", "aaa_bbb_ccc_a_b_c_ab_ba")
        message = "Please note that we are only checking for the sum in this test case which we will extract from your answer. Thus, if you have the same sum as the expected answer, the autograder should have marked this as correct even if the rest of the answer differs from the expected answer. We're printing the sequence from both the expected and your answer so you can compare them and use it if needs be (but the sequence is not necessarily unique).\nWe expected this:\n" + expected + "\nWe got this:\n" + output

        expected = expected.split('_')[0]
        output = output.split('_')[0]
        
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)

    @weight(0.2)
    def test_case50(self):
        # Title used by Gradescope 
        """Test Case 50: Tests rename_people()"""

        expected = "12_1_6_2_1_3_3_4_5_5_2_6_4"
        output = rename_people(6, "aaaaaa_aa_a_ab_abab_abaab", "aaa_aaaaa_a_aaa_aaaaaaaa_aaaaaaaaaa")
        message = "Please note that we are only checking for the sum in this test case which we will extract from your answer. Thus, if you have the same sum as the expected answer, the autograder should have marked this as correct even if the rest of the answer differs from the expected answer. We're printing the sequence from both the expected and your answer so you can compare them and use it if needs be (but the sequence is not necessarily unique).\nWe expected this:\n" + expected + "\nWe got this:\n" + output

        expected = expected.split('_')[0]
        output = output.split('_')[0]
        
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)

    @weight(0.2)
    def test_case51(self):
        # Title used by Gradescope 
        """Test Case 51: Tests rename_people()"""

        expected = "61_1_1_2_2"
        output = rename_people(2, "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx_xxxxxxxxxxxxxxxxxxxxx", "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx_xxxxxx")
        message = "Please note that we are only checking for the sum in this test case which we will extract from your answer. Thus, if you have the same sum as the expected answer, the autograder should have marked this as correct even if the rest of the answer differs from the expected answer. We're printing the sequence from both the expected and your answer so you can compare them and use it if needs be (but the sequence is not necessarily unique).\nWe expected this:\n" + expected + "\nWe got this:\n" + output

        expected = expected.split('_')[0]
        output = output.split('_')[0]
        
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)

    @weight(0.2)
    def test_case52(self):
        # Title used by Gradescope 
        """Test Case 52: Tests rename_people()"""

        expected = "3_1_8_2_2_3_9_4_12_5_1_6_5_7_7_8_4_9_6_10_10_11_3_12_13_13_11"
        output = rename_people(13, "q_r_c_r_j_g_j_k_z_u_w_u_e", "g_n_y_h_g_z_f_l_a_p_b_r_p")
        message = "Please note that we are only checking for the sum in this test case which we will extract from your answer. Thus, if you have the same sum as the expected answer, the autograder should have marked this as correct even if the rest of the answer differs from the expected answer. We're printing the sequence from both the expected and your answer so you can compare them and use it if needs be (but the sequence is not necessarily unique).\nWe expected this:\n" + expected + "\nWe got this:\n" + output

        expected = expected.split('_')[0]
        output = output.split('_')[0]
        
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)

    @weight(0.2)
    def test_case53(self):
        # Title used by Gradescope 
        """Test Case 53: Tests rename_people()"""

        expected = "0"
        output = rename_people(0, "", "")
        message = "Please note that we are only checking for the sum in this test case which we will extract from your answer. Thus, if you have the same sum as the expected answer, the autograder should have marked this as correct even if the rest of the answer differs from the expected answer. We're printing the sequence from both the expected and your answer so you can compare them and use it if needs be (but the sequence is not necessarily unique).\nWe expected this:\n" + expected + "\nWe got this:\n" + output

        expected = expected.split('_')[0]
        output = output.split('_')[0]
        
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)

    @weight(0.2)
    def test_case54(self):
        # Title used by Gradescope 
        """Test Case 54: Tests rename_people()"""

        expected = "0_1_1"
        output = rename_people(1, "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "abcde") 
        message = "Please note that we are only checking for the sum in this test case which we will extract from your answer. Thus, if you have the same sum as the expected answer, the autograder should have marked this as correct even if the rest of the answer differs from the expected answer. We're printing the sequence from both the expected and your answer so you can compare them and use it if needs be (but the sequence is not necessarily unique).\nWe expected this:\n" + expected + "\nWe got this:\n" + output

        expected = expected.split('_')[0]
        output = output.split('_')[0]
        
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)

    @weight(0.2)
    def test_case55(self):
        # Title used by Gradescope 
        """Test Case 55: Tests rename_people()"""

        expected = "5_1_1"
        output = rename_people(1, "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "xxxxx")
        message = "Please note that we are only checking for the sum in this test case which we will extract from your answer. Thus, if you have the same sum as the expected answer, the autograder should have marked this as correct even if the rest of the answer differs from the expected answer. We're printing the sequence from both the expected and your answer so you can compare them and use it if needs be (but the sequence is not necessarily unique).\nWe expected this:\n" + expected + "\nWe got this:\n" + output

        expected = expected.split('_')[0]
        output = output.split('_')[0]
        
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)

    @weight(0.2)
    def test_case56(self):
        # Title used by Gradescope 
        """Test Case 56: Tests rename_people()"""

        expected = "0_1_1"
        output = rename_people(1, "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "")
        message = "Please note that we are only checking for the sum in this test case which we will extract from your answer. Thus, if you have the same sum as the expected answer, the autograder should have marked this as correct even if the rest of the answer differs from the expected answer. We're printing the sequence from both the expected and your answer so you can compare them and use it if needs be (but the sequence is not necessarily unique).\nWe expected this:\n" + expected + "\nWe got this:\n" + output

        expected = expected.split('_')[0]
        output = output.split('_')[0]
        
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)

    @weight(0.2)
    def test_case57(self):
        # Title used by Gradescope 
        """Test Case 57: Tests rename_people()"""

        expected = "0_1_1"
        output = rename_people(1, "x", "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz")
        message = "Please note that we are only checking for the sum in this test case which we will extract from your answer. Thus, if you have the same sum as the expected answer, the autograder should have marked this as correct even if the rest of the answer differs from the expected answer. We're printing the sequence from both the expected and your answer so you can compare them and use it if needs be (but the sequence is not necessarily unique).\nWe expected this:\n" + expected + "\nWe got this:\n" + output

        expected = expected.split('_')[0]
        output = output.split('_')[0]
        
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)

    @weight(0.2)
    def test_case58(self):
        # Title used by Gradescope 
        """Test Case 58: Tests rename_people()"""

        expected = "1_1_1"
        output = rename_people(1, "x", "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        message = "Please note that we are only checking for the sum in this test case which we will extract from your answer. Thus, if you have the same sum as the expected answer, the autograder should have marked this as correct even if the rest of the answer differs from the expected answer. We're printing the sequence from both the expected and your answer so you can compare them and use it if needs be (but the sequence is not necessarily unique).\nWe expected this:\n" + expected + "\nWe got this:\n" + output

        expected = expected.split('_')[0]
        output = output.split('_')[0]
        
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)

    @weight(0.2)
    def test_case59(self):
        # Title used by Gradescope 
        """Test Case 59: Tests rename_people()"""

        expected = "4_1_2_2_1_3_3"
        output = rename_people(3, "yyyyy_acccs_asdnj", "skd_yyyyaccc_dsdjksnj")
        message = "Please note that we are only checking for the sum in this test case which we will extract from your answer. Thus, if you have the same sum as the expected answer, the autograder should have marked this as correct even if the rest of the answer differs from the expected answer. We're printing the sequence from both the expected and your answer so you can compare them and use it if needs be (but the sequence is not necessarily unique).\nWe expected this:\n" + expected + "\nWe got this:\n" + output

        expected = expected.split('_')[0]
        output = output.split('_')[0]
        
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)

    @weight(0.2)
    def test_case60(self):
        # Title used by Gradescope 
        """Test Case 60: Tests rename_people()"""

        expected = "11_1_1_2_2_3_3_4_4"
        output = rename_people(4, "hda_sdn_sndm_sfmn", "hdands_sdnmsdn_snsfdm_sfmdmsn")
        message = "Please note that we are only checking for the sum in this test case which we will extract from your answer. Thus, if you have the same sum as the expected answer, the autograder should have marked this as correct even if the rest of the answer differs from the expected answer. We're printing the sequence from both the expected and your answer so you can compare them and use it if needs be (but the sequence is not necessarily unique).\nWe expected this:\n" + expected + "\nWe got this:\n" + output

        expected = expected.split('_')[0]
        output = output.split('_')[0]
        
        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)

    @weight(0.25)
    def test_case61(self):
        # Title used by Gradescope 
        """Test Case 61: Tests rename_people()"""

        expected = "17_1_8_2_10_3_5_4_7_5_6_6_4_7_2_8_9_9_3_10_1"
        output = rename_people(10, "baa_a_ba_aabab_aa_baab_bb_abbbb_a_a", "a_ba_ba_baabbb_ba_a_aabb_baa_ab_b")
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output

        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)

    @weight(0.25)
    def test_case62(self):
        # Title used by Gradescope 
        """Test Case 62: Tests rename_people()"""

        expected = "11_1_3_2_5_3_4_4_1_5_2"
        output = rename_people(5, "gennady_galya_boris_bill_toshik", "bilbo_torin_gendalf_smaug_galadriel")
        message = "We expected this:\n" + expected + "\nWe got this:\n" + output

        # Standard unit test case with an associated error message 
        self.assertTrue( output == expected, msg=message)

    runTime = time.time() - start_time
