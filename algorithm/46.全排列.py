#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-02-14 23:49:38
LastEditTime: 2022-02-14 23:51:39
Description: 
FilePath: 46.全排列.py
'''
#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        per = []
        for num in nums:
            per.append(per + [num])
        return per
# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    arguments = [[1, 2, 3]]
    for i, args in enumerate(arguments):
        print("=== *{:02d} INPUT* ===".format(i + 1))
        print(args)
        print("=== *DEBUG* ===")
        answer = solution.permute(args)
        print("=== *{:02d} OUTPUT* ===".format(i + 1))
        print(answer)
