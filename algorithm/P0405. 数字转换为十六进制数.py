#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-03 22:39:16
LastEditTime: 2022-02-03 22:56:07
Description:
FilePath: 405.数字转换为十六进制数.py
"""
#
# @lc app=leetcode.cn id=405 lang=python3
#
# [405] 数字转换为十六进制数
#

from string import ascii_lowercase
# @lc code=start
from string import digits

class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        else:
            base = digits + ascii_lowercase[:6]
            if num < 0:
                num = 2 ** 32 - abs(num) 
            hexadecimal = ""
            while num > 0:
                num, mod = divmod(num, 16)
                hexadecimal += base[mod]
            return hexadecimal[::-1]


# @lc code=end
if __name__ == "__main__":
    s = Solution()
    print(s.toHex(26))
    print(s.toHex(-1))
    print(s.toHex(0))
