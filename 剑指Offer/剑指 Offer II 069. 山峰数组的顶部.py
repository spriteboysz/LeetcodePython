#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-18 23:03:26
LastEditTime: 2022-05-18 23:03:27
Description: 
FilePath: 剑指 Offer II 069. 山峰数组的顶部.py
"""

from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        for i in range(1, len(arr) - 1):
            if arr[i - 1] < arr[i] > arr[i + 1]:
                return i


if __name__ == "__main__":
    solution = Solution()
    ans = solution.peakIndexInMountainArray(
        arr=[24, 69, 100, 99, 79, 78, 67, 36, 26, 19]
    )
    print(ans)
    ans = solution.peakIndexInMountainArray(arr=[0, 10, 5, 2])
    print(ans)
