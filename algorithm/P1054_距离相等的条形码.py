#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-05 18:08:51
LastEditTime: 2022-03-05 18:14:07
Description: 
FilePath: 1054.距离相等的条形码.py
"""
#
# @lc app=leetcode.cn id=1054 lang=python3
#
# [1054] 距离相等的条形码
#


# @lc code=start
from collections import defaultdict
from math import ceil
from typing import List


class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        codenum = defaultdict(int)
        for item in barcodes:
            codenum[item] += 1

        barcodes = sorted(barcodes, key=lambda el: (codenum[el], el), reverse=True)
        # print(barcodes)
        mid = ceil(len(barcodes) / 2)
        barcodes[::2], barcodes[1::2] = barcodes[:mid], barcodes[mid:]
        return barcodes


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.rearrangeBarcodes([1, 1, 1, 2, 2])
    print(ans)
    ans = solution.rearrangeBarcodes([2, 2, 1, 3])
    print(ans)
    ans = solution.rearrangeBarcodes([1, 1, 2])
    print(ans)
