#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-12 17:41
LastEditTime: 2022-06-12 17:41
Description:
FilePath: 1802.有界数组中指定下标处的最大值.py
"""


class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        remain, value = maxSum - n, 1
        left, right = index, index
        while left > 0 or right < n - 1:
            remain -= right - left + 1
            if remain < 0:
                return value
            value += 1
            left, right = max(0, left - 1), min(n - 1, right + 1)
        return value + remain // n


if __name__ == '__main__':
    solution = Solution()
    ans = solution.maxValue(4, 2, 6)
    print(ans)
