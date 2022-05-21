#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-21 21:59:18
LastEditTime: 2022-05-21 22:00:59
Description: 
FilePath: 剑指 Offer 44. 数字序列中某一位的数字.py
"""


class Solution:
    def findNthDigit(self, n: int) -> int:
        i = 1
        while i * (10 ** i) < n:
            n += 10 ** i
            i += 1
        return int(str(n // i)[n % i])


if __name__ == "__main__":
    solution = Solution()
    ans = solution.findNthDigit(110)
    print(ans)
