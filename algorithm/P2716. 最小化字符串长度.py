#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-06-24 22:30
FileName: algorithm/P2716. 最小化字符串长度.py
Description: 
"""


class Solution:
    def minimizedStringLength(self, s: str) -> int:
        return len(set(s))


if __name__ == '__main__':
    print(Solution().minimizedStringLength("aaabc"))
