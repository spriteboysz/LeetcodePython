#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-01 21:21:44
LastEditTime: 2022-02-01 21:33:42
Description:
FilePath: 504.七进制数.py
"""
#
# @lc app=leetcode.cn id=504 lang=python3
#
# [504] 七进制数
#

# @lc code=start


class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        else:
            symbol = "-" if num < 0 else ""
            num = abs(num)
            n7 = ""
            while num > 0:
                num, mod = divmod(num, 7)
                n7 += str(mod)
            return symbol + n7[::-1]

# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.convertToBase7(100))
    print(s.convertToBase7(-7))
