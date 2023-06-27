#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-10 21:59:40
LastEditTime: 2022-02-10 22:03:23
Description:
FilePath: 1447.最简分数.py
"""
#
# @lc app=leetcode.cn id=1447 lang=python3
#
# [1447] 最简分数
#

from math import gcd
# @lc code=start
from typing import List


class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        fractions = []
        for i in range(2, n + 1):
            for j in range(1, i):
                if gcd(i, j) == 1:
                    fractions.append(str(j) + "/" + str(i))
        return fractions


# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.simplifiedFractions(3))
    print(s.simplifiedFractions(4))
