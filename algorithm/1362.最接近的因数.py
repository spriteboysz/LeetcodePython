#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-05 15:45:35
LastEditTime: 2022-03-05 15:53:35
Description: 
FilePath: 1362.最接近的因数.py
"""
#
# @lc app=leetcode.cn id=1362 lang=python3
#
# [1362] 最接近的因数
#

# @lc code=start
from typing import List


class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        def closest(num):
            for i in range(int(num ** 0.5), 0, -1):
                if num % i == 0:
                    return i, num // i

        a, b = closest(num + 1)
        c, d = closest(num + 2)
        return [a, b] if b - a < d - c else [c, d]


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.closestDivisors(8)
    print(ans)
    ans = solution.closestDivisors(123)
    print(ans)
    ans = solution.closestDivisors(999)
    print(ans)
