#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-02-12 17:04:55
LastEditTime: 2022-02-12 17:10:25
Description: 
FilePath: 1833.雪糕的最大数量.py
'''
#
# @lc app=leetcode.cn id=1833 lang=python3
#
# [1833] 雪糕的最大数量
#

# @lc code=start
from typing import List


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        count = 0
        for cost in sorted(costs):
            if cost <= coins:
                coins -= cost
                count += 1
            else:
                break
        return count
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.maxIceCream([10, 6, 8, 7, 7, 8], 5))
    print(s.maxIceCream([1, 6, 3, 1, 2, 5], 20))
