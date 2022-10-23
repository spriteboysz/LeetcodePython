#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-10-23 15:21
FileName: algorithm/P2315. 统计星号.py
Description: 
"""


class Solution:
    def countAsterisks(self, s: str) -> int:
        rod, cnt = 0, 0
        for c in s:
            if c == "|":
                rod += 1
            if rod % 2 == 0 and c == "*":
                cnt += 1
        return cnt


if __name__ == '__main__':
    solution = Solution().countAsterisks("yo|ua*|e**|b|e***au|tifu|l")
    print(solution)
