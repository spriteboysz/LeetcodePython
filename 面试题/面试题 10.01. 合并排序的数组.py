#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-02 14:06:51
LastEditTime: 2022-05-02 14:06:51
Description: 
FilePath: 面试题 10.01. 合并排序的数组.py
"""
from typing import List


class Solution:
    def merge(self, A: List[int], m: int, B: List[int], n: int) -> None:
        """
        Do not return anything, modify A in-place instead.
        """
        A[m:] = B
        A.sort()


if __name__ == "__main__":
    solution = Solution()
    ans = solution.merge(A=[1, 2, 3, 0, 0, 0], m=3, B=[2, 5, 6], n=3)
    print(ans)
