#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-06 21:46:46
LastEditTime: 2022-02-06 22:19:37
Description:
FilePath: 1252.奇数值单元格的数目.py
"""
#
# @lc app=leetcode.cn id=1252 lang=python3
#
# [1252] 奇数值单元格的数目
#

# @lc code=start
from typing import List


class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        rows, columns = [0] * m, [0] * n
        for index in indices:
            rows[index[0]] += 1
            columns[index[1]] += 1

        count = 0
        for i in range(m):
            for j in range(n):
                if (rows[i] + columns[j]) % 2:
                    count += 1
        return count

# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.oddCells(2, 3, [[0, 1], [1, 1]]))
    print(s.oddCells(2, 2, [[1, 1], [0, 0]]))
