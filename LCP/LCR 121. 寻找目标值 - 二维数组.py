#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-10-02 23:04
FileName: LCP
Description:LCR 121. 寻找目标值 - 二维数组.py 
"""
from typing import List


class Solution:
    def findTargetIn2DPlants(self, plants: List[List[int]], target: int) -> bool:
        for plant in plants:
            if target in plant:
                return True
        return False


if __name__ == '__main__':
    print(Solution().findTargetIn2DPlants(plants=[[2, 3, 6, 8], [4, 5, 8, 9], [5, 9, 10, 12]], target=8))
