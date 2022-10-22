#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-12 16:49:55
LastEditTime: 2022-02-12 17:01:16
Description:
FilePath: 1828.统计一个圆中点的数目.py
"""

from collections import Counter
from typing import List


class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        points = Counter(map(tuple, points))
        counts = [0] * len(queries)
        for i, query in enumerate(queries):
            for point, v in points.items():
                if (query[0] - point[0]) ** 2 + (query[1] - point[1]) ** 2 <= query[2] ** 2:
                    counts[i] += v
        return counts


if __name__ == "__main__":
    s = Solution()
    print(s.countPoints(points=[[1, 3], [3, 3], [5, 3], [2, 2]],
                        queries=[[2, 3, 1], [4, 3, 1], [1, 1, 2]]))
    print(s.countPoints(points=[[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],
                        queries=[[1, 2, 2], [2, 2, 2], [4, 3, 2], [4, 3, 3]]))
