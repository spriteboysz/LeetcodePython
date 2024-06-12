#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-06-12 21:58
FileName: algorithm
Description:P3174. 清除数字.py 
"""


class Solution:
    def clearDigits(self, s: str) -> str:
        ss = ""
        for c in s:
            if c.isdigit():
                if len(ss) > 0:
                    ss = ss[:-1]
            else:
                ss += c
        return ss


if __name__ == '__main__':
    print(Solution().clearDigits(s="cb34"))
