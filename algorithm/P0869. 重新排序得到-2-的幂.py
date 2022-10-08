#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-14 19:12:30
LastEditTime: 2022-03-14 19:21:56
Description: 
FilePath: 869.重新排序得到-2-的幂.py
"""
#
# @lc app=leetcode.cn id=869 lang=python3
#
# [869] 重新排序得到 2 的幂
#

# @lc code=start
from collections import defaultdict


class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        powercount = defaultdict(list)
        for num in [2 ** i for i in range(30)]:
            temp = [0] * 10
            for item in str(num):
                temp[int(item)] += 1
            powercount[(tuple(temp))].append(num)

        temp = [0] * 10
        for item in str(n):
            temp[int(item)] += 1
        return tuple(temp) in powercount


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.reorderedPowerOf2(2014)
    print(ans)
