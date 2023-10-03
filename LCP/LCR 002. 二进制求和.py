#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-10-01 20:18
FileName: LCP
Description:LCR 002. 二进制求和.py 
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ss = ""
        carry = 0
        while a or b or carry > 0:
            if a:
                carry += int(a[-1])
                a = a[:-1]
            if b:
                carry += int(b[-1])
                b = b[:-1]
            ss = str(carry % 2) + ss
            carry //= 2
        return ss


if __name__ == '__main__':
    print(Solution().addBinary(a="1010", b="1011"))
