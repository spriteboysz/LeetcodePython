#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-25 22:01
LastEditTime: 2022-05-25 22:01
Description:
FilePath: 面试题 16.06. 最小差.py
"""

from typing import List


class Solution:
    def smallestDifference(self, a: List[int], b: List[int]) -> int:
        a.sort()
        b.sort()
        n, m, i, j, minimum = len(a), len(b), 0, 0, 2147483647
        while i < n and j < m:
            minimum = min(minimum, abs(a[i] - b[j]))
            if a[i] > b[j]:
                j += 1
            else:
                i += 1
        return minimum


if __name__ == '__main__':
    solution = Solution()
    ans = solution.smallestDifference([1, 3, 15, 11, 2], [23, 127, 235, 19, 8])
    print(ans)
