#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-07 23:19
LastEditTime: 2022-06-07 23:19
Description:
FilePath: 面试题 16.21. 交换和.py
"""

from typing import List

class Solution:
    def findSwapValues(
            self,
            array1: List[int],
            array2: List[int]) -> List[int]:
        sum1, sum2 = sum(array1), sum(array2)
        if (sum1 + sum2) % 2 != 0:
            return []
        delta = (sum1 + sum2) // 2 - sum1

        set1, set2 = set(array1), set(array2)
        for num in set1:
            if num + delta in set2:
                return [num, num + delta]
        return []

if __name__ == '__main__':
    solution = Solution()
    ans = solution.findSwapValues(
        array1=[4, 1, 2, 1, 1, 2],
        array2=[3, 6, 3, 3])
    print(ans)
