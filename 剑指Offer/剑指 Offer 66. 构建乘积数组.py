#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-10 21:39
LastEditTime: 2022-06-10 21:39
Description:
FilePath: 剑指 Offer 66. 构建乘积数组.py
"""

from typing import List


class Solution:
    def constructArr(self, nums: List[int]) -> List[int]:
        n = len(nums)
        r1, r2 = [1] * n, [1] * n
        for i in range(n - 1):
            r1[i + 1] = r1[i] * nums[i]
        for i in range(n - 1, 0, -1):
            r2[i - 1] = r2[i] * nums[i]

        return [r1[i] * r2[i] for i in range(n)]


if __name__ == '__main__':
    solution = Solution()
    ans = solution.constructArr([1, 2, 3, 4, 5])
    print(ans)
