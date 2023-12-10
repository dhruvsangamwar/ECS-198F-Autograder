import unittest
import time
import collections
from gradescope_utils.autograder_utils.decorators import weight, number, visibility

from assignment7 import predict_tree_height
from assignment7 import k_wrapped_books
from assignment7 import rearrange_bracelet
from assignment7 import second_longest_prefix

runTime = 0.0

class TestDiff(unittest.TestCase):
    global runTime
    start_time = time.time()

    @weight(0.1)
    def test_1(self):
        target_tree_coordinates = [1,1]
        all_trees = [(2,3), (5,5), (1,2), (3,1), (4,4)]
        all_heights = [95, 103.56, 97.22, 107.39, 108.22]
        k = 2
        val = predict_tree_height(target_tree_coordinates, all_trees, all_heights, k)
        self.assertEqual(val, 102.305)

    @weight(0.1)
    def test_2(self):
        target_tree_coordinates = [1,1]
        all_trees = [(2,3), (5,5), (1,2), (3,1), (4,4)]
        all_heights = [95, 103.56, 97.22, 107.39, 108.22]
        k = 3
        val = predict_tree_height(target_tree_coordinates, all_trees, all_heights, k)
        self.assertEqual(val, 299.61)

    @weight(0.1)
    def test_3(self):
        target_tree_coordinates = [1,1]
        all_trees = [(2,3), (5,5), (1,2), (3,1), (4,4)]
        all_heights = [95, 103.56, 97.22, 107.39, 108.22]
        k = 1
        val = predict_tree_height(target_tree_coordinates, all_trees, all_heights, k)
        self.assertEqual(val, 97.22)

    @weight(0.1)
    def test_4(self):
        target_tree_coordinates = [1,1]
        all_trees = [(2,3), (5,5), (1,2), (3,1), (4,4)]
        all_heights = [95, 103.56, 97.22, 107.39, 108.22]
        k = 6
        val = predict_tree_height(target_tree_coordinates, all_trees, all_heights, k)
        self.assertEqual(val, -1)
    
    @weight(0.1)
    def test_5(self):
        target_tree_coordinates = [1,1]
        all_trees = [(2,3), (5,5), (1,2), (3,1), (4,4)]
        all_heights = [95, 103.56, 97.22, 107.39, 108.22]
        k = 4
        val = predict_tree_height(target_tree_coordinates, all_trees, all_heights, k)
        self.assertEqual(val, 101.9575)

    @weight(0.1)
    def test_6(self):
        target_tree_coordinates = [1,1]
        all_trees = [(2,3), (5,5), (1,2), (3,1), (4,4)]
        all_heights = [95, 103.56, 97.22, 107.39, 108.22]
        k = 5
        val = predict_tree_height(target_tree_coordinates, all_trees, all_heights, k)
        self.assertEqual(val, 102.278)

    @weight(0.1)
    def test_7(self):
        target_tree_coordinates = [10,15]
        all_trees = [(20,25), (12,12), (12,16), (13,14), (15,15), (10,10)]
        all_heights = [55, 65.4,78.9, 88.2, 111, 98]
        k = 7
        val = predict_tree_height(target_tree_coordinates, all_trees, all_heights, k)
        self.assertEqual(val, -1)

    @weight(0.1)
    def test_8(self):
        target_tree_coordinates = [10,15]
        all_trees = [(20,25), (12,12), (12,16), (13,14), (15,15), (10,11)]
        all_heights = [55, 65.4, 78.9, 88.2, 111, 98]
        k = 1
        val = predict_tree_height(target_tree_coordinates, all_trees, all_heights, k)
        self.assertEqual(val, 78.9)
    
    @weight(0.1)
    def test_9(self):
        target_tree_coordinates = [10,15]
        all_trees = [(20,25), (12,12), (12,16), (13,14), (15,15), (10,11)]
        all_heights = [55, 65.4, 78.9, 88.2, 111, 98]
        k = 2
        val = predict_tree_height(target_tree_coordinates, all_trees, all_heights, k)
        self.assertEqual(val, 83.55)

    @weight(0.1)
    def test_10(self):
        target_tree_coordinates = [10,15]
        all_trees = [(20,25), (12,12), (12,16), (13,14), (15,15), (10,11)]
        all_heights = [55, 65.4, 78.9, 88.2, 111, 98]
        k = 3
        val = predict_tree_height(target_tree_coordinates, all_trees, all_heights, k)
        self.assertEqual(val, 77.5)

    @weight(0.1)
    def test_11(self):
        target_tree_coordinates = [10,15]
        all_trees = [(20,25), (12,12), (12,16), (13,14), (15,15), (10,11)]
        all_heights = [55, 65.4, 78.9, 88.2, 111, 98]
        k = 4
        val = predict_tree_height(target_tree_coordinates, all_trees, all_heights, k)
        self.assertEqual(val, 82.625)
    
    @weight(0.1)
    def test_12(self):
        target_tree_coordinates = [10,15]
        all_trees = [(20,25), (12,12), (12,16), (13,14), (15,15), (10,11)]
        all_heights = [55, 65.4, 78.9, 88.2, 111, 98]
        k = 5
        val = predict_tree_height(target_tree_coordinates, all_trees, all_heights, k)
        self.assertEqual(val, 88.3)
    
    @weight(0.1)
    def test_13(self):
        target_tree_coordinates = [10,15]
        all_trees = [(20,25), (12,12), (12,16), (13,14), (15,15), (10,11)]
        all_heights = [55, 65.4, 78.9, 88.2, 111, 98]
        k = 6
        val = predict_tree_height(target_tree_coordinates, all_trees, all_heights, k)
        self.assertEqual(val, 82.75)

    @weight(0.1)
    def test_14(self):
        target_tree_coordinates = [0,0]
        all_trees = [(3,3), (2,2), (1,1), (5,5)]
        all_heights = [10, 20, 30, 40]
        k = 5
        val = predict_tree_height(target_tree_coordinates, all_trees, all_heights, k)
        self.assertEqual(val, -1)
    
    @weight(0.1)
    def test_15(self):
        target_tree_coordinates = [0,0]
        all_trees = [(3,3), (2,2), (1,1), (5,5)]
        all_heights = [10, 20, 30, 40]
        k = 1
        val = predict_tree_height(target_tree_coordinates, all_trees, all_heights, k)
        self.assertEqual(val, 30)
    
    @weight(0.1)
    def test_16(self):
        target_tree_coordinates = [0,0]
        all_trees = [(3,3), (2,2), (1,1), (5,5)]
        all_heights = [10, 20, 30, 40]
        k = 2
        val = predict_tree_height(target_tree_coordinates, all_trees, all_heights, k)
        self.assertEqual(val, 25)
    
    @weight(0.1)
    def test_17(self):
        target_tree_coordinates = [0,0]
        all_trees = [(3,3), (2,2), (1,1), (5,5)]
        all_heights = [10, 20, 30, 40]
        k = 3
        val = predict_tree_height(target_tree_coordinates, all_trees, all_heights, k)
        self.assertEqual(val, 20)
    
    @weight(0.1)
    def test_18(self):
        target_tree_coordinates = [0,0]
        all_trees = [(3,3), (2,2), (1,1), (5,5)]
        all_heights = [10, 20, 30, 40]
        k = 4
        val = predict_tree_height(target_tree_coordinates, all_trees, all_heights, k)
        self.assertEqual(val, 25)
    
    @weight(0.1)
    def test_19(self):
        target_tree_coordinates = [5.5,5.5]
        all_trees = [(6.5,6.5), (8.5,5.5), (4.5,4), (10,0), (5,2), (6,4)]
        all_heights = [10,20,10.5,21,10,20]
        k = 7
        val = predict_tree_height(target_tree_coordinates, all_trees, all_heights, k)
        self.assertEqual(val, -1)
    
    @weight(0.1)
    def test_20(self):
        target_tree_coordinates = [5.5,5.5]
        all_trees = [(6.5,6.5), (8.5,5.5), (4.5,4), (10,0), (5,2), (6,4)]
        all_heights = [10,20,10.5,21,10,20]
        k = 1
        val = predict_tree_height(target_tree_coordinates, all_trees, all_heights, k)
        self.assertEqual(val, 10)
    
    @weight(0.1)
    def test_21(self):
        target_tree_coordinates = [5.5,5.5]
        all_trees = [(6.5,6.5), (8.5,5.5), (4.5,4), (10,0), (5,2), (6,4)]
        all_heights = [10,20,10.5,21,10,20]
        k = 2
        val = predict_tree_height(target_tree_coordinates, all_trees, all_heights, k)
        self.assertEqual(val, 15)
    
    @weight(0.1)
    def test_22(self):
        target_tree_coordinates = [5.5,5.5]
        all_trees = [(6.5,6.5), (8.5,5.5), (4.5,4), (10,0), (5,2), (6,4)]
        all_heights = [10,20,10.5,21,10,20]
        k = 3
        val = predict_tree_height(target_tree_coordinates, all_trees, all_heights, k)
        self.assertEqual(val, 13.5)
    
    @weight(0.1)
    def test_23(self):
        target_tree_coordinates = [5.5,5.5]
        all_trees = [(6.5,6.5), (8.5,5.5), (4.5,4), (10,0), (5,2), (6,4)]
        all_heights = [10,20,10.5,21,10,20]
        k = 4
        val = predict_tree_height(target_tree_coordinates, all_trees, all_heights, k)
        self.assertEqual(val, 15.125)
    
    @weight(0.1)
    def test_24(self):
        target_tree_coordinates = [5.5,5.5]
        all_trees = [(6.5,6.5), (8.5,5.5), (4.5,4), (10,0), (5,2), (6,4)]
        all_heights = [10,20,10.5,21,10,20]
        k = 5
        val = predict_tree_height(target_tree_coordinates, all_trees, all_heights, k)
        self.assertEqual(val, 14.1)
    
    @weight(0.1)
    def test_25(self):
        target_tree_coordinates = [5.5,5.5]
        all_trees = [(6.5,6.5), (8.5,5.5), (4.5,4), (10,0), (5,2), (6,4)]
        all_heights = [10,20,10.5,21,10,20]
        k = 6
        val = predict_tree_height(target_tree_coordinates, all_trees, all_heights, k)
        self.assertEqual(val, 15.25)
    
    @weight(0.1)
    def test_26(self):
        unwrap = [1,3,2]
        k = 1
        val = k_wrapped_books(unwrap, k)
        self.assertEqual(val, 2)
    
    @weight(0.1)
    def test_27(self):
        unwrap = [4, 1, 2, 3]
        k = 2
        val = k_wrapped_books(unwrap, k)
        self.assertEqual(val, 2)
    
    @weight(0.1)
    def test_28(self):
        unwrap = [1,2,3]
        k = 1
        val = k_wrapped_books(unwrap, k)
        self.assertEqual(val, -1)
    
    @weight(0.1)
    def test_29(self):
        unwrap = [4,8,1,3,2,5,6,7]
        k = 3
        val = k_wrapped_books(unwrap, k)
        self.assertEqual(val, 2)
    
    @weight(0.1)
    def test_30(self):
        unwrap = [4,8,1,3,2,5,6,7]
        k = 2
        val = k_wrapped_books(unwrap, k)
        self.assertEqual(val, 3)
    
    @weight(0.1)
    def test_31(self):
        unwrap = [4,8,1,3,2,5,6,7]
        k = 4
        val = k_wrapped_books(unwrap, k)
        self.assertEqual(val, -1)
    
    @weight(0.1)
    def test_32(self):
        unwrap = [4,8,1,3,2,5,6,7]
        k = 1
        val = k_wrapped_books(unwrap, k)
        self.assertEqual(val, 4)
    
    @weight(0.1)
    def test_33(self):
        unwrap = [4,8,1,3,2,5,6,7]
        k = 0
        val = k_wrapped_books(unwrap, k)
        self.assertEqual(val, 4)
    
    @weight(0.1)
    def test_34(self):
        unwrap = [1,5,2,4,3]
        k = 5
        val = k_wrapped_books(unwrap, k)
        self.assertEqual(val, -1)
    
    @weight(0.1)
    def test_35(self):
        unwrap = [1,5,2,4,3]
        k = 3
        val = k_wrapped_books(unwrap, k)
        self.assertEqual(val, 2)
    
    @weight(0.1)
    def test_36(self):
        unwrap = [1,5,2,4,3]
        k = 2
        val = k_wrapped_books(unwrap, k)
        self.assertEqual(val, 3)
    
    @weight(0.1)
    def test_37(self):
        unwrap = [1,5,2,4,3]
        k = 0
        val = k_wrapped_books(unwrap, k)
        self.assertEqual(val, 3)
    
    @weight(0.1)
    def test_38(self):
        unwrap = [1,5,2,4,3]
        k = 1
        val = k_wrapped_books(unwrap, k)
        self.assertEqual(val, 4)
    
    @weight(0.1)
    def test_39(self):
        unwrap = [10,6,1,4,8,9,2,3,5,7]
        k = 3
        val = k_wrapped_books(unwrap, k)
        self.assertEqual(val,2)
    
    @weight(0.1)
    def test_40(self):
        unwrap = [10,6,1,4,8,9,2,3,5,7]
        k = 4
        val = k_wrapped_books(unwrap, k)
        self.assertEqual(val,3)
    
    @weight(0.1)
    def test_41(self):
        unwrap = [10,6,1,4,8,9,2,3,5,7]
        k = 2
        val = k_wrapped_books(unwrap, k)
        self.assertEqual(val,4)
    
    @weight(0.1)
    def test_42(self):
        unwrap = [10,6,1,4,8,9,2,3,5,7]
        k = 1
        val = k_wrapped_books(unwrap, k)
        self.assertEqual(val,4)
    
    @weight(0.1)
    def test_43(self):
        unwrap = [10,6,1,4,8,9,2,3,5,7]
        k = 0
        val = k_wrapped_books(unwrap, k)
        self.assertEqual(val,6)
    
    @weight(0.1)
    def test_44(self):
        unwrap = [10,6,1,4,8,9,2,3,5,7]
        k = 7
        val = k_wrapped_books(unwrap, k)
        self.assertEqual(val,-1)
    
    @weight(0.1)
    def test_45(self):
        unwrap = [5,8,6,7,1,3,4,2]
        k = 2
        val = k_wrapped_books(unwrap, k)
        self.assertEqual(val,2)
    
    @weight(0.1)
    def test_46(self):
        unwrap = [5,8,6,7,1,3,4,2]
        k = 1
        val = k_wrapped_books(unwrap, k)
        self.assertEqual(val,3)
    
    @weight(0.1)
    def test_47(self):
        unwrap = [5,8,6,7,1,3,4,2]
        k = 0
        val = k_wrapped_books(unwrap, k)
        self.assertEqual(val,3)
    
    @weight(0.1)
    def test_48(self):
        unwrap = [5,8,6,7,1,3,4,2]
        k = 3
        val = k_wrapped_books(unwrap, k)
        self.assertEqual(val,5)
    
    @weight(0.1)
    def test_49(self):
        unwrap = [5,8,6,7,1,3,4,2]
        k = 4
        val = k_wrapped_books(unwrap, k)
        self.assertEqual(val,-1)
    
    @weight(0.1)
    def test_50(self):
        unwrap = [1,2,3]
        k = 0
        val = k_wrapped_books(unwrap, k)
        self.assertEqual(val,2)
    
    @weight(0.1)
    def test_51(self):
        bracelet = "ccbbaa"
        k = 3
        val = rearrange_bracelet(bracelet, k)
        self.assertIn(val, ['cabcab', 'abcabc', 'bacbac', 'bcabca', 'cbacba', 'acbacb'])
    
    @weight(0.1)
    def test_52(self):
        bracelet = "eeefg"
        k = 3
        val = rearrange_bracelet(bracelet, k)
        self.assertEqual(val,"")
    
    @weight(0.1)
    def test_53(self):
        bracelet = "eeefg"
        k = 2
        val = rearrange_bracelet(bracelet, k)
        self.assertIn(val, ['egefe', 'efege'])
    
    @weight(0.1)
    def test_54(self):
        bracelet = "aaadbbcc"
        k = 3
        val = rearrange_bracelet(bracelet, k)
        self.assertIn(val, ['abcadbac', 'abdcabca', 'acbdabca', 'acbdacba', 'abcadbca', 'abcadcab', 'bacbacda', 'bacbadca', 'acdabcab', 'adbacbac', 'acbadcba', 'abdacbac', 'abcadcba', 'acdbacba', 'acbacdab', 'abcdabca', 'cabdabca', 'acbacbad', 'adcabcab', 'acbadbac', 'cabcabda', 'dacbacba', 'acbacbda', 'abcabcad', 'acbadbca', 'adcbacba', 'abcabcda', 'bacdacba', 'abcdacba', 'dabcabca', 'abcabdac', 'acbadcab', 'adbcabca', 'cabdacba', 'acbacdba', 'cadbacba', 'cabcadba', 'abcabdca', 'badcabca', 'bacdabca'])
    
    @weight(0.1)
    def test_55(self):
        bracelet = "ccbbaa"
        k = 2
        val = rearrange_bracelet(bracelet, k)
        self.assertIn(val, ['cbacba', 'cbabca', 'cbcaba', 'bacacb', 'babcac', 'acbacb', 'acbcba', 'acbabc', 'abcbac', 'abcacb', 'bacbca', 'cacbab', 'bacabc', 'cbabac', 'bacbac', 'bcacab', 'bcabac', 'cabcab', 'abacbc', 'abcabc', 'cabacb', 'bcacba', 'acabcb', 'bcbaca', 'bcabca', 'abcbca', 'acbcab', 'cabcba', 'cababc', 'cbacab'])
    
    @weight(0.1)
    def test_56(self):
        bracelet = "bcdedbb"
        k = 2
        val = rearrange_bracelet(bracelet, k)
        self.assertIn(val, ['bdbebdc', 'bcbdedb', 'dbdcbeb', 'dbcbedb', 'bdbecdb', 'cdbdbeb', 'dcbebdb', 'bdcdbeb', 'dbcdbeb', 'bdebcbd', 'bdbecbd', 'debdbcb', 'dbcebdb', 'cbdbebd', 'bcdbebd', 'cebdbdb', 'cbdebdb', 'cbdbedb', 'ebdcbdb', 'bcebdbd', 'cbedbdb', 'bdbcdeb', 'edbcbdb', 'bebdbcd', 'bdbcbed', 'dbecbdb', 'bdbcedb', 'dbebcbd', 'bdcbdbe', 'ebcbdbd', 'bcbdbde', 'bdedbcb', 'dbdbecb', 'cdbebdb', 'dbdbcbe', 'bdbdecb', 'ebdbcbd', 'debcbdb', 'bcedbdb', 'ecbdbdb', 'bdcebdb', 'bedbcdb', 'bebcdbd', 'bedcbdb', 'bdecbdb', 'dbebdbc', 'bcdebdb', 'bcbedbd', 'ebdbdbc', 'bcbdbed', 'bebdcbd', 'bdcbdeb', 'bdbdcbe', 'dbdbceb', 'dbdebcb', 'ebdbcdb', 'cbdbdbe', 'bdbcbde', 'bcbdebd', 'bdbebcd', 'dcbdbeb', 'cbdbdeb', 'bdbedcb', 'dbcbebd', 'edbdbcb', 'becdbdb', 'bdbdebc', 'bedbdcb', 'dbedbcb', 'bdebdcb', 'bebdbdc', 'bedbcbd', 'dbebdcb', 'bdbcdbe', 'becbdbd', 'bdbdceb', 'dbebcdb', 'bdcbedb', 'cbebdbd', 'dbcbdeb', 'bedbdbc', 'bebdcdb', 'dbcbdbe', 'ebcdbdb', 'bdbcebd', 'ebdbdcb', 'bdebcdb', 'bdebdbc', 'bdbdbce', 'bdcbebd', 'bdbdbec', 'bcdbdeb', 'dbdbebc', 'bdbedbc', 'bcdbdbe', 'bcdbedb'])
    
    @weight(0.1)
    def test_57(self):
        bracelet = "bcdedbb"
        k = 3
        val = rearrange_bracelet(bracelet, k)
        self.assertIn(val, ['bcdbedb', 'bdebcdb', 'bdebdcb', 'bdcbdeb', 'bedbcdb', 'bdcbedb'])
    
    @weight(0.1)
    def test_58(self):
        bracelet = "bcdedbbec"
        k = 4
        val = rearrange_bracelet(bracelet, k)
        self.assertIn(val, ['becdbecdb', 'bcedbcedb', 'bdecbdecb', 'bdcebdceb', 'bcdebcdeb', 'bedcbedcb'])
    
    @weight(0.1)
    def test_59(self):
        bracelet = "ajjabba"
        k = 2
        val = rearrange_bracelet(bracelet, k)
        self.assertIn(val, ['abjbaja', 'jajbaba', 'ajabjab', 'ajbajba', 'abjabja', 'bajajba', 'ajbjaba', 'ajabajb', 'ababjaj', 'ajbabaj', 'bjabaja', 'jabajab', 'bajabja', 'jababja', 'bajabaj', 'ajbajab', 'ajabjba', 'abjajab', 'abjajba', 'jababaj', 'babajaj', 'ajajbab', 'abajajb', 'ajababj', 'jabjaba', 'jajabab', 'babjaja', 'jbabaja', 'abajabj', 'jbajaba', 'jabajba', 'ajbabja', 'abajbja', 'bajajab', 'bjajaba', 'abjabaj', 'abajbaj', 'bajbaja'])
    
    @weight(0.1)
    def test_60(self):
        bracelet = "ajjabba"
        k = 3
        val = rearrange_bracelet(bracelet, k)
        self.assertIn(val, ['ajbajba', 'abjabja'])
    
    @weight(0.1)
    def test_61(self):
        bracelet = "jkjkffjk"
        k = 3
        val = rearrange_bracelet(bracelet, k)
        self.assertIn(val, ['jkfjkfjk', 'kjfkjfkj'])
    
    @weight(0.1)
    def test_62(self):
        bracelet = "jkjkffjk"
        k = 2
        val = rearrange_bracelet(bracelet, k)
        self.assertIn(val, ['jkjfjkfk', 'fjkfjkjk', 'kjfkjkfj', 'jkjkfkfj', 'fkfjkjkj', 'kfjkjkjf', 'kjkfjkfj', 'jkfjkfkj', 'kjfjkjkf', 'fkjkjfjk', 'jkfkjfjk', 'kfkjfjkj', 'jkfjkjkf', 'jfkjkjkf', 'jfkjkfjk', 'kjfjfkjk', 'kfjkjfjk', 'kfjkjkfj', 'fjkjkfjk', 'kjkfjkjf', 'fkjkjkjf', 'kjfjkfjk', 'jkjkfjkf', 'jfkjkfkj', 'fjkjkjfk', 'jfjkjkfk', 'kjkfjfkj', 'jkfkfjkj', 'jfkfkjkj', 'kfjkfjkj', 'jfjkfkjk', 'kjkjfkjf', 'jkjfkfjk', 'jkjfkfkj', 'fkjkjfkj', 'jkjkjfkf', 'jkfkjkjf', 'kfkjkjfj', 'kjfkjfkj', 'kjkjfjfk', 'kfjfjkjk', 'fjkfkjkj', 'kfjkjfkj', 'fkjkjkfj', 'kjkjkfjf', 'jkfjfkjk', 'kjfjkfkj', 'kfjfkjkj', 'fkjkfjkj', 'fkjfjkjk', 'fkjfkjkj', 'kjkjfkfj', 'jkfjkjfk', 'jkjfkjfk', 'jfkfjkjk', 'jfkjkjfk', 'jkjfkjkf', 'jkjkfkjf', 'jkfkjfkj', 'fjkjkfkj', 'kjfjkjfk', 'kjfkjkjf', 'fjkjkjkf', 'fjkjfkjk', 'fjfkjkjk', 'kjfkfjkj', 'kjkfjfjk', 'kjkfkjfj', 'jkjkfjfk', 'jkfkjkfj', 'jkfjkfjk', 'jfkjfkjk', 'kjkjfjkf', 'kjfkjfjk'])
    
    @weight(0.1)
    def test_63(self):
        bracelet = "pggwswp"
        k = 3
        val = rearrange_bracelet(bracelet, k)
        self.assertIn(val, ['wgspgwp', 'spgwpgw', 'gwpswpg', 'pwgpsgw', 'gpwspwg', 'wpgspwg', 'pgwpsgw', 'wsgpwgp', 'pwsgwpg', 'wgpwgsp', 'wpgswpg', 'pwgpswg', 'pwgpwgs', 'pwgspwg', 'swpgwpg', 'sgpwgpw', 'pgwpgws', 'gpwgpsw', 'gpwgspw', 'pgwpswg', 'gwpswgp', 'pgswgpw', 'gpwspgw', 'wpgwpgs', 'wgspwgp', 'swgpwgp', 'pwgswpg', 'pwgpwsg', 'gwpgwsp', 'gwspgwp', 'pgwpgsw', 'wgpswpg', 'pgswpgw', 'pwsgpwg', 'gwpsgpw', 'wspgwpg', 'gwpgspw', 'pwgswgp', 'gspwgpw', 'wpgwsgp', 'pgwsgwp', 'pgwsgpw', 'gwpsgwp', 'wgpwsgp', 'gswpgwp', 'wpsgpwg', 'psgwpgw', 'wgpswgp', 'wpgspgw', 'gpwsgwp', 'gwpgswp', 'gwspwgp', 'pwgspgw', 'wgpsgpw', 'pswgpwg', 'gpwgswp', 'gpwsgpw', 'wgpwgps', 'pgwspwg', 'gwpgwps', 'gpswgpw', 'wpgwpsg', 'wgpsgwp', 'wpgswgp', 'wgpwspg', 'pgwspgw', 'gpswpgw', 'spwgpwg', 'sgwpgwp', 'gpwgpws', 'wpgwspg', 'wpsgwpg'])
    
    @weight(0.1)
    def test_64(self):
        bracelet = "pggwswp"
        k = 4
        val = rearrange_bracelet(bracelet, k)
        self.assertIn(val, ['wpgswpg', 'pwgspwg', 'gwpsgwp', 'wgpswgp', 'gpwsgpw', 'pgwspgw'])
    
    @weight(0.1)
    def test_65(self):
        bracelet = "pggwswp"
        k = 5
        val = rearrange_bracelet(bracelet, k)
        self.assertEqual(val,"")
    
    @weight(0.1)
    def test_66(self):
        bracelet = "igwiwatt"
        k = 5
        val = rearrange_bracelet(bracelet, k)
        self.assertIn(val, ['wtigawti', 'witgawit', 'tiwgatiw', 'twigatwi', 'wtiagwti', 'iwtgaiwt', 'itwagitw', 'twiagtwi', 'itwgaitw', 'tiwagtiw', 'iwtagiwt', 'witagwit'])
    
    @weight(0.1)
    def test_67(self):
        bracelet = "abbccj"
        k = 2
        val = rearrange_bracelet(bracelet, k)
        self.assertIn(val, ['bcbcaj', 'jbcbca', 'cabjbc', 'bcbjac', 'cabcjb', 'cabjcb', 'jbcabc', 'cbcjab', 'bcabcj', 'cbabjc', 'cajbcb', 'bcbjca', 'babcjc', 'jcbacb', 'bcajbc', 'ajbcbc', 'bjacbc', 'cjbacb', 'jcbcba', 'bcjabc', 'cbjcba', 'cabcbj', 'bcbcja', 'cjbcba', 'abcbjc', 'jacbcb', 'cbjacb', 'abcbcj', 'bcacbj', 'bcabjc', 'bacbjc', 'abcjcb', 'jbcbac', 'bjcabc', 'bjcbca', 'bcjbca', 'jcbabc', 'bacjbc', 'cbcabj', 'cbcbaj', 'cbcajb', 'bjbcac', 'acbcjb', 'cjcbab', 'acbcbj', 'acjbcb', 'cbacjb', 'jcabcb', 'bjcbac', 'abcjbc', 'cjabcb', 'jbacbc', 'bajcbc', 'ajcbcb', 'bjcacb', 'cacbjb', 'bcbacj', 'bcbajc', 'cjbabc', 'abjcbc', 'cbajbc', 'cbajcb', 'bcajcb', 'cbacbj', 'jabcbc', 'bcjacb', 'cbjabc', 'bcacjb', 'bacbcj', 'bacjcb', 'cjbcab', 'cbjbac', 'bcjcba', 'jcbcab', 'cbabcj', 'acbjbc', 'cbcbja', 'cbjcab', 'cbjbca', 'cbcjba', 'bcjbac', 'bcjcab', 'jbcacb', 'acbjcb'])
    
    @weight(0.1)
    def test_68(self):
        bracelet = "abbccj"
        k = 3
        val = rearrange_bracelet(bracelet, k)
        self.assertIn(val, ['cbajbc', 'cbjcab', 'jcbacb', 'cbjcba', 'bacbjc', 'cjbacb', 'cabjcb', 'bcjbca', 'cjbcab', 'jbcabc', 'cbacbj', 'bjcabc', 'cbjacb', 'bcajcb', 'bcjabc', 'bcajbc', 'cabcjb', 'bacjbc', 'bcjbac', 'cbjabc', 'bcabjc', 'bcabcj', 'bjcbac', 'cbacjb', 'bcjacb', 'abcjbc', 'cbajcb', 'acbjcb'])
    
    @weight(0.1)
    def test_69(self):
        bracelet = "abbccj"
        k = 4
        val = rearrange_bracelet(bracelet, k)
        self.assertIn(val, ['bcjabc', 'cbajcb', 'cbjacb', 'bcajbc'])
    
    @weight(0.1)
    def test_70(self):
        bracelet = "abbccj"
        k = 5
        val = rearrange_bracelet(bracelet, k)
        self.assertEqual(val,"")
    
    @weight(0.1)
    def test_71(self):
        bracelet = "ghghjhg"
        k = 2
        val = rearrange_bracelet(bracelet, k)
        self.assertIn(val, ['ghghghj', 'gjhghgh', 'hghjghg', 'jghghgh', 'ghgjhgh', 'ghghjgh', 'hjghghg', 'hghghjg', 'hghghgj', 'hgjhghg', 'hghgjgh', 'ghghjhg', 'hgjghgh', 'hghgjhg', 'ghghgjh', 'ghjghgh', 'jhghghg', 'ghjhghg'])
    
    @weight(0.1)
    def test_72(self):
        bracelet = "lmnjjk"
        k = 4
        val = rearrange_bracelet(bracelet, k)
        self.assertIn(val, ['jnklmj', 'jknlmj', 'kjlnmj', 'jnkmjl', 'mjklnj', 'jmnljk', 'mjnklj', 'kjlmnj', 'jlkmjn', 'jlnkmj', 'jknmjl', 'mjlknj', 'jmknjl', 'njklmj', 'jlnmjk', 'ljknmj', 'ljkmnj', 'jmklnj', 'jklnjm', 'jlnmkj', 'jmlnjk', 'jklmnj', 'jkmljn', 'jklmjn', 'jnmklj', 'jkmnlj', 'jmknlj', 'jnlkmj', 'jmnklj', 'njmklj', 'njlkmj', 'njkmlj', 'jlkmnj', 'jmnlkj', 'jnlmjk', 'jkmnjl', 'ljnkmj', 'jnkljm', 'jlmkjn', 'mjknlj', 'jlmknj', 'jlknmj', 'jnmljk', 'jlmnkj', 'jlknjm', 'ljmknj', 'jmkljn', 'jnkmlj', 'mjlnkj', 'ljmnkj', 'njlmkj', 'njmlkj', 'jmnkjl', 'jnmlkj', 'jkmlnj', 'kjnmlj', 'jlnkjm', 'jnmkjl', 'jklnmj', 'kjmlnj', 'jnlkjm', 'jnlmkj', 'ljnmkj', 'mjnlkj', 'jmlkjn', 'jknljm', 'kjmnlj', 'kjnlmj', 'jknmlj', 'jmlnkj', 'jmlknj', 'jlmnjk'])

    @weight(0.1)
    def test_73(self):
        bracelet = "abbccj"
        k = 5
        val = rearrange_bracelet(bracelet, k)
        self.assertIn(val, ['jkmlnj', 'jnmklj', 'jknmlj', 'jklnmj', 'jmklnj', 'jlnkmj', 'jklmnj', 'jkmnlj', 'jnlmkj', 'jmlknj', 'jlkmnj', 'jlmnkj', 'jmlnkj', 'jlknmj', 'jknlmj', 'jmnklj', 'jnkmlj', 'jnmlkj', 'jmnlkj', 'jlmknj', 'jmknlj', 'jlnmkj', 'jnlkmj', 'jnklmj'])
    
    @weight(0.1)
    def test_74(self):
        bracelet = "lmnjjkc"
        k = 6
        val = rearrange_bracelet(bracelet, k)
        self.assertIn(val, ['jkcnlmj', 'jcmlknj', 'jnmclkj', 'jcnkmlj', 'jcmnklj', 'jmlnkcj', 'jckmlnj', 'jlcknmj', 'jmcklnj', 'jnmklcj', 'jckmnlj', 'jkcnmlj', 'jncmklj', 'jmclknj', 'jnlkmcj', 'jmklncj', 'jmknlcj', 'jncmlkj', 'jlnkmcj', 'jcmlnkj', 'jcnlkmj', 'jnclmkj', 'jmnklcj', 'jnmlkcj', 'jknlcmj', 'jmknclj', 'jlnckmj', 'jklcmnj', 'jnmcklj', 'jkcmlnj', 'jknclmj', 'jknmlcj', 'jmnlkcj', 'jlknmcj', 'jnlmckj', 'jlkncmj', 'jnklmcj', 'jlckmnj', 'jmnclkj', 'jklcnmj', 'jmklcnj', 'jmncklj', 'jmcnklj', 'jknmclj', 'jkclmnj', 'jklmcnj', 'jncklmj', 'jnlckmj', 'jmkcnlj', 'jlmkncj', 'jclnkmj', 'jklnmcj', 'jcmnlkj', 'jmkclnj', 'jkmnlcj', 'jcnmlkj', 'jlmnkcj', 'jlmcknj', 'jnklcmj', 'jlnkcmj', 'jclnmkj', 'jnkmlcj', 'jnlkcmj', 'jlmnckj', 'jmnlckj', 'jkmclnj', 'jcmklnj', 'jkmcnlj', 'jnkmclj', 'jklncmj', 'jlcmnkj', 'jknlmcj', 'jlmcnkj', 'jlcnmkj', 'jmcknlj', 'jnckmlj', 'jnmlckj', 'jmcnlkj', 'jnlcmkj', 'jmclnkj', 'jlnmckj', 'jkncmlj', 'jnkcmlj', 'jnkclmj', 'jlkcmnj', 'jcklnmj', 'jcmknlj', 'jmnkclj', 'jlkcnmj', 'jlncmkj', 'jclkmnj', 'jclknmj', 'jcnklmj', 'jclmnkj', 'jnlmkcj', 'jkmlcnj', 'jclmknj', 'jlmkcnj', 'jkclnmj', 'jlkmncj', 'jkcmnlj', 'jcnmklj', 'jmlcknj', 'jnclkmj', 'jlcmknj', 'jkmlncj', 'jmlnckj', 'jkmnclj', 'jlcnkmj', 'jlkmcnj', 'jcklmnj', 'jlnmkcj', 'jnmkclj', 'jcknmlj', 'jmlkncj', 'jmlkcnj', 'jcnlmkj', 'jcknlmj', 'jmlcnkj', 'jklmncj'])
    
    @weight(0.1)
    def test_75(self):
        bracelet = "ywfyggt"
        k = 5
        val = rearrange_bracelet(bracelet, k)
        self.assertIn(val, ['ygtwfyg', 'ygwtfyg', 'gytwfgy', 'ygwftyg', 'gywftgy', 'ygftwyg', 'ygtfwyg', 'gytfwgy', 'ygfwtyg', 'gyftwgy', 'gywtfgy', 'gyfwtgy'])
    
    @weight(0.1)
    def test_76(self):
        text = "ssiencss"
        val = second_longest_prefix(text)
        self.assertEqual(val,"s")

    @weight(0.1)
    def test_77(self):
        text = "ababab"
        val = second_longest_prefix(text)
        self.assertEqual(val,"ab")
    
    @weight(0.1)
    def test_78(self):
        text = "sciences"
        val = second_longest_prefix(text)
        self.assertEqual(val,"")
    
    @weight(0.1)
    def test_79(self):
        text = "aaaaa"
        val = second_longest_prefix(text)
        self.assertEqual(val,"aaa")
    
    @weight(0.1)
    def test_80(self):
        text = "abbabba"
        val = second_longest_prefix(text)
        self.assertEqual(val,"a")
    
    @weight(0.1)
    def test_81(self):
        text = "abcdefg"
        val = second_longest_prefix(text)
        self.assertEqual(val,"")
    
    @weight(0.1)
    def test_82(self):
        text = "ababababab"
        val = second_longest_prefix(text)
        self.assertEqual(val,"ababab")
    
    @weight(0.1)
    def test_83(self):
        text = "abababab"
        val = second_longest_prefix(text)
        self.assertEqual(val,"abab")
    
    @weight(0.1)
    def test_84(self):
        text = "ababab"
        val = second_longest_prefix(text)
        self.assertEqual(val,"ab")
    
    @weight(0.1)
    def test_85(self):
        text = "babab"
        val = second_longest_prefix(text)
        self.assertEqual(val,"b")
    
    @weight(0.1)
    def test_86(self):
        text = "bababa"
        val = second_longest_prefix(text)
        self.assertEqual(val,"ba")
    
    @weight(0.1)
    def test_87(self):
        text = "baba"
        val = second_longest_prefix(text)
        self.assertEqual(val,"")
    
    @weight(0.1)
    def test_88(self):
        text = "bbbcccbbb"
        val = second_longest_prefix(text)
        self.assertEqual(val,"bb")
    
    @weight(0.1)
    def test_89(self):
        text = "bbbcccbb"
        val = second_longest_prefix(text)
        self.assertEqual(val,"b")
    
    @weight(0.1)
    def test_90(self):
        text = "bbbcccb"
        val = second_longest_prefix(text)
        self.assertEqual(val,"")
    
    @weight(0.1)
    def test_91(self):
        text = "bbbbbb"
        val = second_longest_prefix(text)
        self.assertEqual(val,"bbbb")
    
    @weight(0.1)
    def test_92(self):
        text = "bbcbb"
        val = second_longest_prefix(text)
        self.assertEqual(val,"b")
    
    @weight(0.1)
    def test_93(self):
        text = "cgacga"
        val = second_longest_prefix(text)
        self.assertEqual(val,"")
    
    @weight(0.1)
    def test_94(self):
        text = "acgacga"
        val = second_longest_prefix(text)
        self.assertEqual(val,"a")
    
    @weight(0.1)
    def test_95(self):
        text = "ffgffgffg"
        val = second_longest_prefix(text)
        self.assertEqual(val,"ffg")
    
    @weight(0.1)
    def test_96(self):
        text = "ffgffg"
        val = second_longest_prefix(text)
        self.assertEqual(val,"")
    
    @weight(0.1)
    def test_97(self):
        text = "jklljk"
        val = second_longest_prefix(text)
        self.assertEqual(val,"")
    
    @weight(0.1)
    def test_98(self):
        text = "ccggcc"
        val = second_longest_prefix(text)
        self.assertEqual(val,"c")
    
    @weight(0.1)
    def test_99(self):
        text = "ccgc"
        val = second_longest_prefix(text)
        self.assertEqual(val,"")
    
    @weight(0.1)
    def test_100(self):
        text = "jjarjj"
        val = second_longest_prefix(text)
        self.assertEqual(val,"j")

    runTime = time.time() - start_time
