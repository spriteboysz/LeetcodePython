#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-18 20:29:27
LastEditTime: 2022-03-18 20:30:02
Description: 
FilePath: 372.超级次方.py
"""
#
# @lc app=leetcode.cn id=372 lang=python3
#
# [372] 超级次方
#

# @lc code=start
from typing import List


class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        power, mod = 1, 1337
        for num in b:
            power = ((power ** 10) % mod) * ((a ** num) % mod)
            power %= mod
        return power


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    ans = solution.superPow(2147483647, [2, 0, 0])
    print(ans)
    ans = solution.superPow(2, [1, 0])
    print(ans)
