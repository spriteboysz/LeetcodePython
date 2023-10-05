#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-10-03 11:44
FileName: LCP
Description:LCR 128. 库存管理 I.py 
"""
from typing import List


class Solution:
    def stockManagement(self, stock: List[int]) -> int:
        return min(stock)


if __name__ == '__main__':
    print(Solution().stockManagement(stock=[4, 5, 8, 3, 4]))
