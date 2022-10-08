#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-26 22:46:16
LastEditTime: 2022-01-26 22:50:42
Description: 
FilePath: 1365.有多少小于当前数字的数字.py
'''
#
# @lc app=leetcode.cn id=1365 lang=python3
#
# [1365] 有多少小于当前数字的数字
#

# @lc code=start
from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sequence = list(sorted(nums))
        small = []
        for item in nums:
            small.append(sequence.index(item))
        return small
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.smallerNumbersThanCurrent([8, 1, 2, 2, 3]))
    print(s.smallerNumbersThanCurrent([6, 5, 4, 8]))
    print(s.smallerNumbersThanCurrent([7, 7, 7, 7]))
