#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-27 22:35:39
LastEditTime: 2022-02-27 22:37:48
Description: 
FilePath: 2080.区间内查询数字的频率.py
"""
#
# @lc app=leetcode.cn id=2080 lang=python3
#
# [2080] 区间内查询数字的频率
#

# @lc code=start
from bisect import bisect_left, bisect_right
from collections import defaultdict
from typing import List


class RangeFreqQuery:
    def __init__(self, arr: List[int]):
        self.counts = defaultdict(list)
        for i, num in enumerate(arr):
            self.counts[num].append(i)

    def query(self, left: int, right: int, value: int) -> int:
        return bisect_right(self.counts[value], right) - bisect_left(
            self.counts[value], left
        )


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)
# @lc code=end
