#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-13 15:28:42
LastEditTime: 2022-02-16 23:06:34
Description:
FilePath: 78.子集.py
"""
#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset = [[]]
        for num in nums:
            for i in range(len(subset)):
                subset.append(subset[i] + [num])
        return subset

# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    arguments = [[1, 2, 3], [0]]
    for i, args in enumerate(arguments):
        print("=== {:02d} INPUT ===".format(i + 1))
        print(args)
        print("=== DEBUG ===")
        answer = solution.subsets(args)
        print("=== OUTPUT ===")
        print(answer)


