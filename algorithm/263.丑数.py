#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-01 20:04:17
Description: 丑数
FilePath: 263.丑数.py
'''
#
# @lc app=leetcode.cn id=263 lang=python3
#
# [263] 丑数
#

# @lc code=start


class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        if n == 1:
            return True
        for element in [2, 3, 5]:
            while n % element == 0:
                n //= element
        return n == 1


# @lc code=end

if __name__ == '__main__':
    s = Solution()
    print(2, s.isUgly(2))
    print(6, s.isUgly(6))
    print(8, s.isUgly(8))
    print(14, s.isUgly(14))
