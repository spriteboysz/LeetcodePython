#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-24 23:23:30
LastEditTime: 2022-01-24 23:34:05
Description: 
FilePath: 1619.删除某些元素后的数组均值.py
'''
#
# @lc app=leetcode.cn id=1619 lang=python3
#
# [1619] 删除某些元素后的数组均值
#

# @lc code=start
from typing import List


class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr = sorted(arr)
        length = len(arr)
        total = sum(arr[int(length * 0.05):int(length * 0.95)])
        return float("%.5f" % (total / (length * 0.9)))
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.trimMean([1, 2, 2, 2, 2, 2, 2, 2,
          2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3]))
