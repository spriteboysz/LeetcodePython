#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-25 00:09:29
LastEditTime: 2022-01-25 22:18:46
Description:
FilePath: 1556.千位分隔数.py
"""
#
# @lc app=leetcode.cn id=1556 lang=python3
#
# [1556] 千位分隔数
#

# @lc code=start


class Solution:
    def thousandSeparator(self, n: int) -> str:
        s = str(n)
        init = len(s) % 3
        num = s[:init]
        for i, item in enumerate(s[init:]):
            if i % 3 == 0:
                num += "."
            num += item
        return num.lstrip(".")

# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.thousandSeparator(12))
