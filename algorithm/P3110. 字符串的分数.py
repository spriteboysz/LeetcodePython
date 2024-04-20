#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-04-20 12:36
FileName: algorithm
Description:P3110. 字符串的分数.py 
"""


class Solution:
    def scoreOfString(self, s: str) -> int:
        nums = [ord(c) for c in s]
        return sum([abs(nums[i] - nums[i - 1]) for i in range(1, len(s))])


if __name__ == '__main__':
    print(Solution().scoreOfString(s="hello"))
