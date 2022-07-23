#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-30 22:01:23
LastEditTime: 2022-03-30 22:03:43
Description: 
FilePath: 2194.excel-表中某个范围内的单元格.py
"""
#
# @lc app=leetcode.cn id=2194 lang=python3
#
# [2194] Excel 表中某个范围内的单元格
#

# @lc code=start
from typing import List
from string import ascii_uppercase as upper


class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        c1, r1, _, c2, r2 = list(s)
        cells = []
        for column in range(upper.index(c1), upper.index(c2) + 1):
            for row in range(int(r1), int(r2) + 1):
                cells.append(upper[column] + str(row))
        return cells


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.cellsInRange("K1:L2")
    print(ans)
    ans = solution.cellsInRange("A1:F1")
    print(ans)
