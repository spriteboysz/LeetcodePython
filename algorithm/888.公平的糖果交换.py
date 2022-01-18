#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-19 00:00:44
LastEditTime: 2022-01-19 00:17:46
Description: 
FilePath: 888.公平的糖果交换.py
'''
#
# @lc app=leetcode.cn id=888 lang=python3
#
# [888] 公平的糖果交换
#

# @lc code=start
from typing import List


class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        aliceSum, bobSum = sum(aliceSizes), sum(bobSizes)
        for a in aliceSizes:
            b = (aliceSum + bobSum) // 2 + a - aliceSum
            if b in bobSizes:
                return [a, b]


# @lc code=end
if __name__ == '__main__':
    s = Solution()
    print(s.fairCandySwap([1, 2], [2, 3]))
    print(s.fairCandySwap([2], [1, 3]))
    print(s.fairCandySwap([1, 2, 5], [2, 4]))
