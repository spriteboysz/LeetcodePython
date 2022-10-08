#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-15 00:02
LastEditTime: 2022-06-15 00:02
Description:
FilePath: 849.到最近的人的最大距离.py
"""

from typing import List


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        index = [0] + [i for i,
                       seat in enumerate(seats) if seat] + [len(seats) - 1]
        left, right = index[1] - index[0], index[-1] - index[-2]
        distance = max(left, right)
        for j in range(1, len(index) - 1):
            distance = max(distance, (index[j + 1] - index[j]) // 2)
        return distance


if __name__ == '__main__':
    solution = Solution()
    ans = solution.maxDistToClosest(seats=[1, 0, 0, 0, 1, 0, 1])
    print(ans)
    ans = solution.maxDistToClosest([1, 0, 0, 0])
    print(ans)
    ans = solution.maxDistToClosest([1, 0])
    print(ans)
