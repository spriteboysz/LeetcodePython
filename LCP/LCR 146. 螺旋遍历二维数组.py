#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-10-04 20:21
FileName: LCP
Description:LCR 146. 螺旋遍历二维数组.py 
"""
from typing import List


class Solution:
    def spiralArray(self, array: List[List[int]]) -> List[int]:
        nums = []
        while array:
            nums += array.pop(0)
            array = list(zip(*array))[::-1]
        return nums


if __name__ == '__main__':
    print(Solution().spiralArray(array=[[1, 2, 3], [8, 9, 4], [7, 6, 5]]))
