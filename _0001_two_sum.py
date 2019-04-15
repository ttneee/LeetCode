from typing import List

class Solution:
    def twoSum(self, int_list, target_int):
        sub_log = {}
        length = len(int_list)
        for index in range(length):
            num = int_list[index]
            sub = target_int - num
            if sub in sub_log:
                return sub_log[sub], index
            else:
                sub_log[num] = index