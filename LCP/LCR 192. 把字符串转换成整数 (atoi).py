#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-10-03 23:16
FileName: LCP
Description:LCR 192. 把字符串转换成整数 (atoi).py 
"""
import re


class Solution:
    def myAtoi(self, s: str) -> int:
        s_num = re.match(r"^[+,-]?[0-9]+", s.strip())
        num = int(s_num.group()) if s_num else 0
        if num < -2147483648:
            return -2147483648
        if num > 2147483647:
            return 2147483647
        return num


if __name__ == '__main__':
    print(Solution().myAtoi("   -42"))
