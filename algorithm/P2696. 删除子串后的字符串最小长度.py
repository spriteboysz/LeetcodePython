#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-06-24 22:53
FileName: algorithm/P2696. 删除子串后的字符串最小长度.py
Description: 
"""


class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        for c in s:
            if len(stack) == 0:
                stack.append(c)
            elif stack[-1] == "A" and c == "B":
                stack.pop()
            elif stack[-1] == "C" and c == "D":
                stack.pop()
            else:
                stack.append(c)
        return len(stack)


if __name__ == '__main__':
    print(Solution().minLength(s="ABFCACDB"))
