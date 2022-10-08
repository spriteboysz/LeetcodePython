#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-13 23:26:06
LastEditTime: 2022-01-13 23:34:45
Description: 
FilePath: 575.分糖果.py
'''
#
# @lc app=leetcode.cn id=575 lang=python3
#
# [575] 分糖果
#

# @lc code=start
from typing import List


class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        n, m = len(candyType), len(set(candyType))
        return n // 2 if m >= n // 2 else m

# @lc code=end


if __name__ == '__main__':
    s = Solution()
    print(s.distributeCandies([1, 1, 2, 3]))
