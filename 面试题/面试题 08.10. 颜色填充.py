#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-02 14:26:48
LastEditTime: 2022-05-02 14:26:48
Description: 
FilePath: 面试题 08.10. 颜色填充.py
"""

from typing import List


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, newColor: int
    ) -> List[List[int]]:
        n, m, init = len(image), len(image[0]), image[sr][sc]

        def dfs(x, y):
            if 0 <= x < n and 0 <= y < m and image[x][y] == init:
                image[x][y] = newColor
                dfs(x - 1, y)
                dfs(x + 1, y)
                dfs(x, y - 1)
                dfs(x, y + 1)

        if init != newColor:
            dfs(sr, sc)
        return image


if __name__ == "__main__":
    solution = Solution()
    ans = solution.floodFill(image=[[1, 1, 1], [1, 1, 0], [1, 0, 1]], sr=1, sc=1, newColor=2)
    print(ans)
    ans = solution.floodFill([[0, 0, 0], [0, 1, 1]], 1, 1, 1)
    print(ans)
