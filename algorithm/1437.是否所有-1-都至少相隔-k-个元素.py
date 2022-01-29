#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-29 22:36:05
LastEditTime: 2022-01-29 22:48:24
Description: 
FilePath: 1437.是否所有-1-都至少相隔-k-个元素.py
'''
#
# @lc app=leetcode.cn id=1437 lang=python3
#
# [1437] 是否所有 1 都至少相隔 k 个元素
#

# @lc code=start
from typing import List
from math import inf


class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        position = []
        minimum = inf
        for i, item in enumerate(nums):
            if item == 1:
                position.append(i)
                if len(position) >= 2 and minimum > position[-1] - position[-2]:
                    minimum = position[-1] - position[-2]
        return minimum - 1 >= k
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.kLengthApart([1, 0, 0, 0, 1, 0, 0, 1], 2))
    print(s.kLengthApart([1, 0, 0, 1, 0, 1], 2))
    print(s.kLengthApart([1, 1, 1, 1, 1], 0))
    print(s.kLengthApart([0, 1, 0, 1], 1))
