#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-14 21:33:59
LastEditTime: 2022-03-14 21:38:52
Description: 
FilePath: 1237.找出给定方程的正整数解.py
"""
#
# @lc app=leetcode.cn id=1237 lang=python3
#
# [1237] 找出给定方程的正整数解
#

# @lc code=start
from typing import List

"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
"""


# class CustomFunction:
#     # Returns f(x, y) for any given positive integers x and y.
#     # Note that f(x, y) is increasing with respect to both x and y.
#     # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
#     def f(self, x, y):
#         return x + y


class Solution:
    def findSolution(self, customfunction: "CustomFunction", z: int) -> List[List[int]]:
        solution = []
        for x in range(1, z + 1):
            for y in range(1, z + 1):
                if customfunction.f(x, y) == z:
                    solution.append([x, y])
        return solution


# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    ans = solution.findSolution(function_id=1, z=5)
    print(ans)
