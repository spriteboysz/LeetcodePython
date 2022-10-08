#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-26 22:41:00
LastEditTime: 2022-02-26 22:44:49
Description:
FilePath: 477.汉明距离总和.py
"""

from typing import List


class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        s_nums = [bin(num)[2:].rjust(32, "0") for num in nums]
        count = 0
        for item in zip(*s_nums):
            count += item.count("1") * item.count("0")
        return count


if __name__ == '__main__':
    solution = Solution()
    ans = solution.totalHammingDistance(nums=[4, 14, 2])
    print(ans)
