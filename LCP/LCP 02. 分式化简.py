#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-23 23:01
LastEditTime: 2022-05-23 23:01
Description:
FilePath: LCP 02. 分式化简.py
"""

from typing import List


class Solution:
    def fraction(self, cont: List[int]) -> List[int]:
        n, m = 0, 1
        for a in cont[::-1]:
            n, m = m, (m * a + n)
        return [m, n]


if __name__ == '__main__':
    solution = Solution()
    ans = solution.fraction([3, 2, 0, 2])
    print(ans)
