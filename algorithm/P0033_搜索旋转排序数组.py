#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-17 17:05:54
LastEditTime: 2022-04-17 17:07:32
Description: 
FilePath: 33.搜索旋转排序数组.py
"""
#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#

# @lc code=
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target not in nums:
            return -1
        else:
            return nums.index(target)


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.search([4, 5, 6, 7, 0, 1, 2], 3)
    print(ans)
