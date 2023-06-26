#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-05 23:49:34
LastEditTime: 2022-02-06 00:09:51
Description:
FilePath: 56.合并区间.py
"""
#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#

# @lc code=start
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        section = [0] * 10002
        for interval in intervals:
            section[interval[0]:interval[1] + 1] = [1] * \
                (interval[1] - interval[0] + 1)
        block = []
        start = 1
        for i in range(1, len(section) - 1):
            if section[i - 1] == 0 and section[i] == 1:
                start = i
            if section[i] == 1 and section[i + 1] == 0:
                end = i
                block.append([start, end])
        return block
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
    print(s.merge([[1, 4], [4, 5], [9, 9], [11, 12]]))
