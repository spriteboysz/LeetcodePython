#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2021-09-26 23:38:27
Description: 有效的完全平方数
FilePath: 367.有效的完全平方数.py
"""
#
# @lc app=leetcode.cn id=367 lang=python3
#
# [367] 有效的完全平方数
#

# @lc code=start
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        for i in range(num + 1):
            if i ** 2 == num:
                return True
            elif i ** 2 > num:
                return False
        return False

# @lc code=end


if __name__ == '__main__':
    s = Solution()
    print(s.isPerfectSquare(16))
