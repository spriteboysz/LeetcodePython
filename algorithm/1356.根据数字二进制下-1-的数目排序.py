#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-26 22:51:39
LastEditTime: 2022-01-26 22:54:12
Description: 
FilePath: 1356.根据数字二进制下-1-的数目排序.py
'''
#
# @lc app=leetcode.cn id=1356 lang=python3
#
# [1356] 根据数字二进制下 1 的数目排序
#

# @lc code=start
from json.tool import main
from typing import List


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return list(sorted(arr, key=lambda el: (bin(el).count("1"), el)))
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.sortByBits([1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]))
