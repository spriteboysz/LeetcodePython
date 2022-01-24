#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-25 00:09:29
LastEditTime: 2022-01-25 00:18:30
Description: 
FilePath: 1556.千位分隔数.py
'''
#
# @lc app=leetcode.cn id=1556 lang=python3
#
# [1556] 千位分隔数
#

# @lc code=start
class Solution:
    def thousandSeparator(self, n: int) -> str:
        length = len(str(n))
        if length <= 3:
            return str(n)
        else:
            start = length % 3
            print(str(n)[start:])
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.thousandSeparator(1234))
