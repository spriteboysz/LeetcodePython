#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-02-05 22:23:55
LastEditTime: 2022-02-05 22:35:05
Description: 
FilePath: 100323.把数组排成最小的数.py
'''
#
# @lc app=leetcode.cn id=100323 lang=python3
#
# [剑指 Offer 45] 把数组排成最小的数
#

# @lc code=start
from typing import List


class Solution:
    def minNumber(self, nums: List[int]) -> str:
        return "".join(sorted(map(str, nums)))
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.minNumber([10, 2]))
    print(s.minNumber([3, 30, 34, 5, 9]))
