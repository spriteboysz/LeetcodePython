#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2021-09-21 15:28:05
Description: 4的幂
FilePath: 342.4的幂.py
"""
#
# @lc app=leetcode.cn id=342 lang=python3
#
# [342] 4的幂
#

# @lc code=start
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        for i in range(n + 1):
            if 4 ** i == n:
                return True
            elif 4 ** i > n:
                return False
        return False

# @lc code=end


if __name__ == '__main__':
    s = Solution()
    print(s.isPowerOfFour(64))
