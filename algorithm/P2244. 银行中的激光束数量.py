#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-08 22:16:03
LastEditTime: 2022-02-08 22:26:30
Description:
FilePath: 2244.银行中的激光束数量.py
"""
#
# @lc app=leetcode.cn id=2244 lang=python3
#
# [2125] 银行中的激光束数量
#

# @lc code=start
from typing import List


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        lasers = []
        for row in bank:
            cur = sum(map(int, row))
            if cur != 0:
                lasers.append(cur)
        count = 0
        for i in range(len(lasers) - 1):
            count += lasers[i] * lasers[i + 1]
        return count
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.numberOfBeams(bank=["011001", "000000", "010100", "001000"]))
    print(s.numberOfBeams(bank=["000", "111", "000"]))
