import unittest
from _0001_two_sum import Solution
from Helpers import CompareHelper


class SolutionTest(unittest.TestCase):

    def is_match(self, value_list, ans_list):
        return len(list(set(value_list) - set(ans_list))) == 0

    def test_twoSum(self):

        s = Solution()

        self.assertTrue(CompareHelper.isListMatch(
            s.twoSum([0, 4, 3, 0], 0), [0, 3]))

        self.assertTrue(CompareHelper.isListMatch(
            s.twoSum([2, 7, 11, 15], 9), [0, 1]))
