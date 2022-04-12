#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-11 23:22:10
LastEditTime: 2022-04-11 23:31:35
Description: 
FilePath: 661.图片平滑器.py
"""
#
# @lc app=leetcode.cn id=661 lang=python3
#
# [661] 图片平滑器
#

# @lc code=start
from typing import List


class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])
        smoother = [[0] * n for _ in range(m)]
        matrix = [(x, y) for x in range(-1, 2) for y in range(-1, 2)]
        for i in range(m):
            for j in range(n):
                values = []
                for x, y in matrix:
                    if 0 <= i + x < m and 0 <= j + y < n:
                        values.append(img[i + x][j + y])
                smoother[i][j] = sum(values) // len(values)
        return smoother


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.imageSmoother([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
    print(ans)
    ans = solution.imageSmoother([[100, 200, 100], [200, 50, 200], [100, 200, 100]])
    print(ans)
