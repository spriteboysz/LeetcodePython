#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-10-03 22:51
FileName: LCP
Description:LCR 158. 库存管理 II.py 
"""
from collections import Counter
from typing import List


class Solution:
    def inventoryManagement(self, stock: List[int]) -> int:
        for k, v in Counter(stock).items():
            if v > len(stock) // 2:
                return k


if __name__ == '__main__':
    print(Solution().inventoryManagement(stock=[6, 1, 3, 1, 1, 1]))
