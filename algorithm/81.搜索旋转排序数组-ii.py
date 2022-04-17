#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-17 17:09:13
LastEditTime: 2022-04-17 17:10:11
Description: 
FilePath: 81.搜索旋转排序数组-ii.py
"""
#
# @lc app=leetcode.cn id=81 lang=python3
#
# [81] 搜索旋转排序数组 II
#

# @lc code=start
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        return target in nums


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.search([2, 5, 6, 0, 0, 1, 2], 0)
    print(ans)
