#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-01-04 23:11
FileName: algorithm
Description:P2937. 使三个字符串相等.py 
"""


class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        maximum = 0
        for a, b, c in zip(s1, s2, s3):
            if len({a, b, c}) > 1:
                break
            maximum += 1
        return -1 if maximum == 0 else len(s1) + len(s2) + len(s3) - maximum * 3


if __name__ == '__main__':
    print(Solution().findMinimumOperations(s1="abc", s2="abb", s3="ab"))
