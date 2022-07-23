#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-16 00:07:56
LastEditTime: 2022-02-18 23:31:16
Description: 
FilePath: 1909.删除一个元素使数组严格递增.py
"""
#
# @lc app=leetcode.cn id=1909 lang=python3
#
# [1909] 删除一个元素使数组严格递增
#

# @lc code=start
from typing import List


class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(len(nums)):
            temp = nums[:i] + nums[i + 1 :]
            if sorted(temp) == temp and len(set(temp)) == n - 1:
                return True
        return False


# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.canBeIncreasing([1, 2, 10, 5, 7]))
    print(s.canBeIncreasing([2, 3, 1, 2]))
    print(s.canBeIncreasing([1, 1, 1]))
    print(s.canBeIncreasing([1, 2, 3]))
    print(s.canBeIncreasing([105, 924, 32, 968]))
