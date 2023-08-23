#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-08-22 23:48
FileName: algorithm
Description:P2810. 故障键盘.py 
"""


class Solution:
    def finalString(self, s: str) -> str:
        ss = ""
        for c in s:
            if c == 'i':
                ss = "".join(list(reversed(ss)))
            else:
                ss += c
        return ss


if __name__ == '__main__':
    print(Solution().finalString(s="string"))
