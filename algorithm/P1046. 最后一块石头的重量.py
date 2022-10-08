#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-29 23:15:26
LastEditTime: 2022-01-29 23:21:18
Description: 
FilePath: 1046.最后一块石头的重量.py
'''
#
# @lc app=leetcode.cn id=1046 lang=python3
#
# [1046] 最后一块石头的重量
#

# @lc code=start
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            diff = stones[-1] - stones[-2]
            stones.pop(-1)
            stones.pop(-1)
            if diff > 0:
                stones.append(diff)
        return stones[0] if len(stones) else 0

# @lc code=end
