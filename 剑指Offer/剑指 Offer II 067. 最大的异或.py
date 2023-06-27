#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-20 23:23
LastEditTime: 2022-06-20 23:23
Description:
FilePath: 剑指 Offer II 067. 最大的异或.py
"""

from typing import List


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        pass


if __name__ == '__main__':
    solution = Solution()
    ans = solution.findMaximumXOR(nums=[3, 10, 5, 25, 2, 8])
    print(ans)
    ans = solution.findMaximumXOR(nums=[14, 70, 53, 83, 49, 91, 36, 80, 92, 51, 66, 70])
    print(ans)
