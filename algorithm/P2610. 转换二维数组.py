#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-06-25 22:02
FileName: algorithm/P2610. 转换二维数组.py
Description: 
"""
from collections import defaultdict
from typing import List


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        matrix, dic = defaultdict(list), defaultdict(int)
        for num in nums:
            matrix[dic[num]].append(num)
            dic[num] += 1
        return list(matrix.values())


if __name__ == '__main__':
    print(Solution().findMatrix(nums=[1, 3, 4, 1, 2, 3, 1]))
