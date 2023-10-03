#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-10-03 22:55
FileName: LCP
Description:LCR 159. 库存管理 III.py 
"""
from typing import List


class Solution:
    def inventoryManagement(self, stock: List[int], cnt: int) -> List[int]:
        return sorted(stock)[:cnt]


if __name__ == '__main__':
    print(Solution().inventoryManagement(stock=[0, 2, 3, 6], cnt=2))
