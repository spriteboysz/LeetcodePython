#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-09-25 23:49
FileName: 面试题
Description:P2864. 最大二进制奇数.py 
"""


class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        cnt0, cnt1 = s.count("0"), s.count("1")
        return "1" * ((cnt1 - 1) if cnt1 > 1 else 0) + "0" * cnt0 + "1"


if __name__ == '__main__':
    print(Solution().maximumOddBinaryNumber(s="0101"))
