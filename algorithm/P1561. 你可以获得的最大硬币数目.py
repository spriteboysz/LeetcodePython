#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-15 22:00:24
LastEditTime: 2022-02-15 22:05:57
Description:
FilePath: 1561.你可以获得的最大硬币数目.py
"""
#
# @lc app=leetcode.cn id=1561 lang=python3
#
# [1561] 你可以获得的最大硬币数目
#

# @lc code=start
from typing import List


class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n = len(piles)
        piles.sort(reverse=True)
        return sum(piles[1:2*n//3:2])
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.maxCoins([2, 4, 1, 2, 7, 8]))
    print(s.maxCoins([2, 4, 5]))
    print(s.maxCoins([9, 8, 7, 6, 5, 1, 2, 3, 4]))
