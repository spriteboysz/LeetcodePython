#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-24 23:11
LastEditTime: 2022-05-24 23:11
Description:
FilePath: 面试题 08.06. 汉诺塔问题.py
"""

from typing import List


class Solution:
    def hanota(self, A: List[int], B: List[int], C: List[int]) -> None:
        """
        Do not return anything, modify C in-place instead.
        """
        def move(n, A, B, C):
            if n == 1:
                C.append(A[-1])
                A.pop()
                return
            else:
                move(n - 1, A, C, B)
                C.append(A[-1])
                A.pop()
                move(n - 1, B, A, C)

        move(len(A), A, B, C)


if __name__ == '__main__':
    solution = Solution()
    ans = solution.hanota(A=[2, 1, 0], B=[], C=[])
    # print(ans)
