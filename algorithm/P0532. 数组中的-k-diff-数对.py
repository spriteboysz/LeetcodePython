#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-12 22:34:58
LastEditTime: 2022-02-12 22:41:16
Description:
FilePath: 532.数组中的-k-diff-数对.py
"""
#
# @lc app=leetcode.cn id=532 lang=python3
#
# [532] 数组中的 k-diff 数对
#

# @lc code=start
from typing import List


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k == 0:
            return len(set([num for num in nums if nums.count(num) >= 2]))
        else:
            temp = [num + k for num in nums]
            return len(set(nums) & set(temp))

# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.findPairs([3, 1, 3, 1, 5], 2))
    print(s.findPairs([1, 2, 3, 4, 5], 1))
    print(s.findPairs([1, 3, 1, 5, 4], 0))
