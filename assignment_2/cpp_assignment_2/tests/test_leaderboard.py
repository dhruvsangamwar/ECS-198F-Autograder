# -*- coding: utf-8 -*-

import unittest
import random
from gradescope_utils.autograder_utils.decorators import leaderboard
from test_subprocess import runTime


class TestLeaderboard(unittest.TestCase):
    def setUp(self):
        pass

    # @leaderboard("accuracy")
    # def test_leaderboard_float(self, set_leaderboard_value=None):
    #     """Sets a leaderboard value"""
    #     set_leaderboard_value(round(random.uniform(50, 100), 2))

    @leaderboard("Time", "asc")
    def test_another(self, set_leaderboard_value=None):

        """Sets a leaderboard value that's sorted ascending (lower is better)"""
        set_leaderboard_value(round(runTime*10000, 3))
