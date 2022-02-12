#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-02-10 23:28:04
LastEditTime: 2022-02-12 22:47:33
Description: 
FilePath: 378.有序矩阵中第-k-小的元素.py
'''
#
# @lc app=leetcode.cn id=378 lang=python3
#
# [378] 有序矩阵中第 K 小的元素
#

# @lc code=start
from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        matrix = sorted(sum(matrix, []))
        return matrix[k - 1]
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.kthSmallest(matrix=[[1, 5, 9], [10, 11, 13], [12, 13, 15]], k=8))
