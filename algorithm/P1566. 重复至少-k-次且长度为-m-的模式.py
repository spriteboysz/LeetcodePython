#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-01 23:24:58
LastEditTime: 2022-02-01 23:39:19
Description:
FilePath: 1566.重复至少-k-次且长度为-m-的模式.py
"""
#
# @lc app=leetcode.cn id=1566 lang=python3
#
# [1566] 重复至少 K 次且长度为 M 的模式
#

# @lc code=start
from typing import List


class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        s = "#".join(map(str, arr))
        for i in range(len(arr) - m):
            if "#".join(list(map(str, arr[i:i+m])) * k) in s:
                return True
        return False
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.containsPattern([1, 2, 4, 4, 4, 4], 1, 3))
    print(s.containsPattern(arr=[1, 2, 1, 2, 1, 1, 1, 3], m=2, k=2))
    print(s.containsPattern(arr=[1, 2, 1, 2, 1, 3], m=2, k=3))
    print(s.containsPattern(arr=[1, 2, 3, 1, 2], m=2, k=2))
    print(s.containsPattern(arr=[2, 2, 2, 2], m=2, k=3))
