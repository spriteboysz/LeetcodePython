#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-18 23:29:37
LastEditTime: 2022-05-18 23:29:37
Description: 
FilePath: abc.py
"""

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        stack = []
        for start, end in sorted(intervals):
            if stack and stack[-1][-1] >= start:
                stack[-1][-1] = max(stack[-1][-1], end)
            else:
                stack.append([start, end])
        return stack


if __name__ == "__main__":
    solution = Solution()
    ans = solution.merge(intervals=[[1, 3], [2, 6], [8, 10], [15, 18]])
    print(ans)
