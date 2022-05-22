#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-22 17:15
LastEditTime: 2022-05-22 17:15
Description:
FilePath: 面试题 16.16. 部分排序.py
"""

from typing import List


class Solution:
    def subSort(self, array: List[int]) -> List[int]:
        array2 = sorted(array[:])
        if array2 == array:
            return [-1, -1]

        i, j = 0, len(array) - 1
        while array2[i] == array[i]:
            i += 1
        while array2[j] == array[j]:
            j -= 1
        return [i, j]


if __name__ == '__main__':
    solution = Solution()
    ans = solution.subSort([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19])
    print(ans)
