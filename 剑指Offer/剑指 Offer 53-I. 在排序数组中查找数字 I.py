#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-01 21:42:50
LastEditTime: 2022-05-01 21:45:51
Description:
FilePath: 剑指 Offer 53 - I. 在排序数组中查找数字 I.py
"""

from bisect import bisect_right, bisect_left
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return bisect_right(nums, target) - bisect_left(nums, target)


if __name__ == "__main__":
    solution = Solution()
    ans = solution.search([1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 5], 3)
    print(ans)
