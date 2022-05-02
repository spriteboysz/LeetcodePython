#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-01 22:45:56
LastEditTime: 2022-05-01 22:48:37
Description: 
FilePath: 剑指 Offer II 075. 数组相对排序.py
"""

from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # def index(num):
        #     if num not in arr2:
        #         return inf
        #     else:
        #         return arr2.index(num)
        return sorted(
            arr1, key=lambda num: arr2.index(num) if num in arr2 else len(arr2) + num
        )


if __name__ == "__main__":
    solution = Solution()
    ans = solution.relativeSortArray(
        arr1=[2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], arr2=[2, 1, 4, 3, 9, 6]
    )
    print(ans)
    ans = solution.relativeSortArray([28, 6, 22, 8, 44, 17], [22, 28, 8, 6])
    print(ans)
