#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-07 22:26:11
LastEditTime: 2022-02-01 22:05:02
Description:
FilePath: 67.二进制求和.py
"""
#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#

# @lc code=start


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) > len(b):
            a, b = b, a
        a = "0" * (len(b) - len(a)) + a
        carry = 0
        c = ""
        for i in range(len(a) - 1, - 1, -1):
            carry, mod = divmod(int(a[i]) + int(b[i]) + carry, 2)
            c += str(mod)
        if carry == 0:
            return c[::-1]
        else:
            return str(carry) + c[::-1]
# @lc code=end


if __name__ == '__main__':
    s = Solution()
    print(s.addBinary("1111", "1"))
    print(s.addBinary("0", "0"))
