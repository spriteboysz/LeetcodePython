#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-10 22:37:45
LastEditTime: 2022-04-10 22:47:33
Description:
FilePath: 84.柱状图中最大的矩形.py
"""

from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights = [0] + heights + [0]
        stack = []
        maximum = 0
        for index, value in enumerate(heights):
            while stack and heights[index] < heights[stack[-1]]:
                area = stack.pop()
                width = index - stack[-1] - 1
                maximum = max(maximum, heights[area] * width)
            stack.append(index)
        return maximum


if __name__ == '__main__':
    solution = Solution()
    print(solution.largestRectangleArea(heights=[2, 1, 5, 6, 2, 3]))
