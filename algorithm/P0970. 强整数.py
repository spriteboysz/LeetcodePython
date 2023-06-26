#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-05 17:45:41
LastEditTime: 2022-03-05 17:58:17
Description:
FilePath: 970.强整数.py
"""
#
# @lc app=leetcode.cn id=970 lang=python3
#
# [970] 强整数
#

from math import log
# @lc code=start
from typing import List

class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        if bound < 2:
            return []
        powerful = set()
        a = int(log(bound, x)) + 1 if x > 1 else 1
        b = int(log(bound, y)) + 1 if y > 1 else 1

        for i in range(a):
            for j in range(b):
                cur = x ** i + y ** j
                if cur > bound:
                    break
                powerful.add(cur)
        return list(powerful)
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.powerfulIntegers(3, 5, 15)
    print(ans)
    ans = solution.powerfulIntegers(2, 3, 0)
    print(ans)

