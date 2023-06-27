#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-12 16:16
LastEditTime: 2022-06-12 16:16
Description:
FilePath: 1785.构成特定和需要添加的最少元素.py
"""

from math import ceil
from typing import List


class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        return ceil(abs(goal - sum(nums)) / limit)


if __name__ == '__main__':
    solution = Solution()
    ans = solution.minElements(nums=[1, -1, 1], limit=3, goal=-4)
    print(ans)
    ans = solution.minElements(nums=[1, -10, 9, 1], limit=100, goal=0)
    print(ans)
