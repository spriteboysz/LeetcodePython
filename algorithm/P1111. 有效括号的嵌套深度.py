#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-07-08 22:58
FileName: algorithm/P1111. 有效括号的嵌套深度.py
Description: 
"""
from typing import List


class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        depths, depth = [], 0
        for c in seq:
            if c == '(':
                depth += 1
                depths.append(depth % 2)
            else:
                depths.append(depth % 2)
                depth -= 1
        return depths


if __name__ == '__main__':
    print(Solution().maxDepthAfterSplit(seq="()(())()"))
