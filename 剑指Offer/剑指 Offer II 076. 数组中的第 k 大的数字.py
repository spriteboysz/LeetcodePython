#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-18 23:21:34
LastEditTime: 2022-05-18 23:23:09
Description: 
FilePath: 剑指 Offer II 076. 数组中的第 k 大的数字.py
"""

from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums, reverse=True)[k - 1]


if __name__ == "__main__":
    solution = Solution()
    ans = solution.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4)
    print(ans)
