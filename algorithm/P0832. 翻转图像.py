#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2021-09-28 23:58:14
Description:
FilePath: 832.翻转图像.py
"""
#
# @lc app=leetcode.cn id=832 lang=python3
#
# [832] 翻转图像
#

# @lc code=start
from typing import List


class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n, m = len(image), len(image[0])
        for i in range(n):
            image[i] = image[i][::-1]
            for j in range(m):
                image[i][j] = int(not image[i][j])
        return image

# @lc code=end


if __name__ == '__main__':
    s = Solution()
    print(s.flipAndInvertImage(
        [[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]))
