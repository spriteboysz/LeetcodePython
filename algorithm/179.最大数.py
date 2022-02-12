#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-02-12 22:17:36
LastEditTime: 2022-02-12 22:33:34
Description: 
FilePath: 179.最大数.py
'''
#
# @lc app=leetcode.cn id=179 lang=python3
#
# [179] 最大数
#

# @lc code=start
from typing import List
from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))
        nums.sort(key=cmp_to_key(lambda x, y: 1 if x + y < y + x else -1))
        return "".join(nums) if nums[0] != "0" else "0"
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.largestNumber([10, 2]))
    print(s.largestNumber([3, 30, 34, 5, 9]))
    print(s.largestNumber([0, 0]))
