#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-05-11 21:25
FileName: algorithm
Description:P2914. 使二进制字符串变美丽的最少修改次数.py 
"""


class Solution:
    def minChanges(self, s: str) -> int:
        return sum([int(bool(s[i] != s[i + 1])) for i in range(0, len(s), 2)])


if __name__ == '__main__':
    print(Solution().minChanges(s="1001"))
