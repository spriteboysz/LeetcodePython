#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-25 22:22:54
LastEditTime: 2022-01-25 22:29:18
Description:
FilePath: 1534.统计好三元组.py
"""
#
# @lc app=leetcode.cn id=1534 lang=python3
#
# [1534] 统计好三元组
#

# @lc code=start
from typing import List


class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        count = 0
        for i in range(len(arr) - 2):
            for j in range(i + 1, len(arr) - 1):
                if abs(arr[i] - arr[j]) <= a:
                    for k in range(j + 1, len(arr)):
                        if abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                            count += 1
        return count

# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.countGoodTriplets([7, 3, 7, 3, 12, 1, 12, 2, 3], 5, 8, 1))
