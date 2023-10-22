import unittest
import time
import collections
from gradescope_utils.autograder_utils.decorators import weight, number, visibility
from linkedList import LinkedList

from assignment2 import detectCycle
from assignment2 import find_next_recommendation

runTime = 0.0

class TestDiff(unittest.TestCase):
    global runTime
    start_time = time.time()

    @weight(10)
    def test_1(self):
        """detectCycle - Test Case 1"""
        my_linked_list = LinkedList()
        my_linked_list.append(1)
        my_linked_list.append(2)
        my_linked_list.append(3)
        my_linked_list.append(4)
        my_linked_list.append(5)
        my_linked_list.create_cycle(2)

        val = detectCycle(my_linked_list)
        self.assertEqual(val, 'True')

    @weight(10)
    def test_2(self):
        """detectCycle - Test Case 2"""
        my_linked_list = LinkedList()
        my_linked_list.append(1) # originally 'a'
        my_linked_list.append(2) # originally 'b'
        my_linked_list.append(3) # originally 'c'
        my_linked_list.append(4) # originally 'd'
        my_linked_list.append(5) # originally 'e'
        my_linked_list.create_cycle(3) # originally 'b'
        
        val = detectCycle(my_linked_list)
        self.assertEqual(val, 'True')

    @weight(10)
    def test_3(self):
        """detectCycle - Test Case 3"""
        my_linked_list = LinkedList()
        my_linked_list.append(1) # originally 'a'
        my_linked_list.append(1) # originally 'a'
        my_linked_list.append(1) # originally 'a'
        my_linked_list.append(1) # originally 'a'
        my_linked_list.append(1) # originally 'a'
        my_linked_list.create_cycle(1) # originally 'a'
        
        val = detectCycle(my_linked_list)
        self.assertEqual(val, 'True')

    @weight(10)
    def test_4(self):
        """detectCycle - Test Case 4"""
        my_linked_list = LinkedList()
        my_linked_list.append(1)
        my_linked_list.append(2)
        my_linked_list.append(3)
        my_linked_list.append(4)
        my_linked_list.append(5)
        
        val = detectCycle(my_linked_list)
        self.assertEqual(val, 'False')
    
    @weight(10)
    def test_5(self):
        """detectCycle - Test Case 5"""
        my_linked_list = LinkedList()
        
        val = detectCycle(my_linked_list)
        self.assertEqual(val, 'False')

    @weight(10)
    def test_6(self):
        """find_next_recommendation - Test Case 1"""

        graph_test1 = {
            'You': {'Friend1': 2, 'Friend2': 3, 'Friend3': 4},
            'Friend1': {'You': 2, 'Friend4': 1},
            'Friend2': {'You': 3, 'Friend5': 2},
            'Friend3': {'You': 4},
            'Friend4': {'Friend1': 1},
            'Friend5': {'Friend2': 2}
        }

        current_friends_test1 = {'Friend1', 'Friend2'}

        val = find_next_recommendation(graph_test1, current_friends_test1)
        self.assertEqual(val, 'Next recommended friend: Friend4')

    @weight(10)
    def test_7(self):
        """find_next_recommendation - Test Case 2"""

        graph_test2 = {
            'You': {'Friend1': 2.5, 'Friend2': 3, 'Friend3': 4.2, 'Friend4': 1.8},
            'Friend1': {'You': 2.5, 'Friend5': 3.1},
            'Friend2': {'You': 3, 'Friend5': 2.8},
            'Friend3': {'You': 4.2, 'Friend6': 2.3},
            'Friend4': {'You': 1.8},
            'Friend5': {'Friend1': 3.1, 'Friend2': 2.8},
            'Friend6': {'Friend3': 2.3}
        }

        current_friends_test2 = {'Friend1', 'Friend2', 'Friend3'}


        val = find_next_recommendation(graph_test2, current_friends_test2)
        self.assertEqual(val, 'Next recommended friend: Friend4')


    @weight(10)
    def test_8(self):
        """find_next_recommendation - Test Case 3"""

        graph_test3 = {
            'You': {},
            'Friend1': {},
            'Friend2': {},
            'Friend3': {},
            'Friend4': {},
            'Friend5': {}
        }

        current_friends_test3 = set()


        val = find_next_recommendation(graph_test3, current_friends_test3)
        self.assertEqual(val, 'Next recommended friend: None')

    @weight(10)
    def test_9(self):
        """find_next_recommendation - Test Case 4"""

        graph_test4 = {
            'You': {'Friend1': 2.5},
            'Friend1': {'You': 2.5},
            'Friend2': {},
            'Friend3': {},
            'Friend4': {},
            'Friend5': {}
        }

        current_friends_test4 = {'Friend1'}



        val = find_next_recommendation(graph_test4, current_friends_test4)
        self.assertEqual(val, 'Next recommended friend: None')

    @weight(10)
    def test_10(self):
        """find_next_recommendation - Test Case 5"""

        graph_test5 = {
            'You': {'Friend1': 3, 'Friend2': 3, 'Friend3': 3, 'Friend4': 3},
            'Friend1': {'You': 3, 'Friend5': 3},
            'Friend2': {'You': 3, 'Friend6': 3},
            'Friend3': {'You': 3, 'Friend7': 3},
            'Friend4': {'You': 3, 'Friend8': 3},
            'Friend5': {'Friend1': 3},
            'Friend6': {'Friend2': 3},
            'Friend7': {'Friend3': 3},
            'Friend8': {'Friend4': 3}
        }

        current_friends_test5 = {'Friend1', 'Friend2', 'Friend3', 'Friend4'}


        val = find_next_recommendation(graph_test5, current_friends_test5)
        self.assertIn(val, ['Next recommended friend: Friend5', 'Next recommended friend: Friend6', 'Next recommended friend: Friend7', 'Next recommended friend: Friend8'])

    runTime = time.time() - start_time

\