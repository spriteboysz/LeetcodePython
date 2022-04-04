#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-04 22:34:40
LastEditTime: 2022-04-04 22:36:25
Description: 
FilePath: 60.排列序列.py
"""
#
# @lc app=leetcode.cn id=60 lang=python3
#
# [60] 排列序列
#

# @lc code=start
from itertools import permutations


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        array = list(permutations(range(1, n + 1), n))
        return "".join(map(str, array[k - 1]))


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.getPermutation(3, 3)
    print(ans)
    ans = solution.getPermutation(4, 9)
    print(ans)
