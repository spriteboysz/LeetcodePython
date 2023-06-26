#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-26 23:51:24
LastEditTime: 2022-01-26 23:55:17
Description:
FilePath: 1299.将每个元素替换为右侧最大元素.py
"""
#
# @lc app=leetcode.cn id=1299 lang=python3
#
# [1299] 将每个元素替换为右侧最大元素
#

# @lc code=start
from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        arr2 = []
        for i in range(1, len(arr)):
            arr2.append(max(arr[i:]))
        arr2.append(-1)
        return arr2
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.replaceElements([17, 18, 5, 4, 6, 1]))
