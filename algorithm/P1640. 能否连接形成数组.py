#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-27 22:46:37
LastEditTime: 2022-01-27 22:55:24
Description:
FilePath: 1640.能否连接形成数组.py
"""
#
# @lc app=leetcode.cn id=1640 lang=python3
#
# [1640] 能否连接形成数组
#

from functools import reduce
# @lc code=start
from typing import List


class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        return arr == reduce(lambda a, b: a + b, sorted(pieces,
                                                        key=lambda el: arr.index(el[0]) if el[0] in arr else -1))


# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.canFormArray([91, 4, 64, 78], [[78], [4, 64], [91]]))
    print(s.canFormArray([1, 3, 5, 7], [[2, 4, 6, 8]]))
