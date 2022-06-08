#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-08 23:13
LastEditTime: 2022-06-08 23:13
Description:
FilePath: 845.数组中的最长山脉.py
"""

from typing import List


class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        maximum = 0
        for i in range(1, len(arr) - 1):
            left, right = i, i
            if arr[i - 1] < arr[i] > arr[i + 1]:
                while left - 1 >= 0 and arr[left] > arr[left - 1]:
                    left -= 1
                while right + 1 < len(arr) and arr[right] > arr[right + 1]:
                    right += 1
                maximum = max(maximum, right - left + 1)
        return maximum


if __name__ == '__main__':
    solution = Solution()
    ans = solution.longestMountain(arr=[2, 1, 4, 7, 3, 2, 5])
    print(ans)
