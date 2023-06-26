#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-10 22:57:21
LastEditTime: 2022-02-10 23:01:25
Description:
FilePath: 347.前-k-个高频元素.py
"""
#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#

# @lc code=start
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = dict()
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        count = sorted(count.items(), key=lambda el: el[1], reverse=True)
        return [el[0] for el in count[:k]]
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.topKFrequent([1, 1, 1, 2, 2, 3], 2))
    print(s.topKFrequent([1], 1))
