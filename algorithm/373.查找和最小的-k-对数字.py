#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-02 23:23:38
LastEditTime: 2022-03-02 23:24:58
Description: 
FilePath: 373.查找和最小的-k-对数字.py
"""
#
# @lc app=leetcode.cn id=373 lang=python3
#
# [373] 查找和最小的 K 对数字
#

# @lc code=start
from heapq import heappush, heappop
from typing import List


class Solution:
    def kSmallestPairs(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> List[List[int]]:
        heap = []
        for a in nums1[:k]:
            for b in nums2[:k]:
                heappush(heap, (-a - b, a, b))
                if len(heap) > k:
                    heappop(heap)
        return [[a, b] for _, a, b in heap]


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.kSmallestPairs([1, 7, 11], [2, 4, 6], 3)
    print(ans)
