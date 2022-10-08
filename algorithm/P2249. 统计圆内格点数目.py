#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-29 17:49
LastEditTime: 2022-05-29 17:49
Description:
FilePath: 2249.统计圆内格点数目.py
"""


from typing import List


class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        points = set()
        for x, y, r in circles:
            for dx in range(-r, r + 1):
                for dy in range(-r, r + 1):
                    if dx * dx + dy * dy <= r * r:
                        points.add((x + dx, y + dy))
        return len(points)


if __name__ == '__main__':
    solution = Solution()
    ans = solution.countLatticePoints(circles=[[2, 2, 2], [3, 4, 1]])
    print(ans)
