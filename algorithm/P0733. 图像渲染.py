#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-11 23:47:29
LastEditTime: 2022-04-11 23:48:39
Description: 
FilePath: 733.图像渲染.py
"""
#
# @lc app=leetcode.cn id=733 lang=python3
#
# [733] 图像渲染
#

# @lc code=start
from typing import List


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, newColor: int
    ) -> List[List[int]]:
        target = image[sr][sc]
        directions = {(1, 0), (-1, 0), (0, 1), (0, -1)}

        def dfs(r, c):
            if target == newColor:
                return
            if 0 <= r < len(image) and 0 <= c < len(image[0]) and image[r][c] == target:
                image[r][c] = newColor
                for x, y in directions:
                    dfs(r + x, c + y)
        dfs(sr, sc)
        return image


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.floodFill(
        image=[[1, 1, 1], [1, 1, 0], [1, 0, 1]], sr=1, sc=1, newColor=2
    )
    print(ans)
    ans = solution.floodFill([[0, 0, 0], [0, 0, 0]], sr=0, sc=0, newColor=2)
    print(ans)
