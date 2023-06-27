#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-01 22:04:51
LastEditTime: 2022-05-01 22:17:31
Description: 
FilePath: 剑指 Offer II 072. 求平方根.py
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        if not x:
            return 0
        left, right = 1, x // 2
        while left < right:
            mid = left + (right - left) // 2
            lower, upper = mid * mid, (mid + 1) * (mid + 1)
            if lower <= x < upper:
                return mid
            elif x < lower:
                right = mid
            else:
                left = mid + 1
        return left


if __name__ == "__main__":
    solution = Solution()
    ans = solution.mySqrt(10)
    print(ans)
    ans = solution.mySqrt(1)
    print(ans)
