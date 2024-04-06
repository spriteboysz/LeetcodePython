#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-04-06 13:17
FileName: algorithm
Description:P3083. 字符串及其反转中是否存在同一子字符串.py 
"""


class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        for i in range(1, len(s)):
            if s[i] + s[i - 1] in s:
                return True
        return False


if __name__ == '__main__':
    print(Solution().isSubstringPresent(s="leetcode"))
