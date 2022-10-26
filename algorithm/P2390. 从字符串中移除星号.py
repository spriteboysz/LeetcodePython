#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-10-26 21:48
FileName: algorithm/P2390. 从字符串中移除星号.py
Description: 
"""


class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for c in s:
            if c == "*":
                stack.pop()
            else:
                stack.append(c)
        return "".join(stack)


if __name__ == '__main__':
    solution = Solution().removeStars("erase*****")
    print(solution)
