#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-11 23:10:00
LastEditTime: 2022-02-11 23:16:42
Description:
FilePath: 1679.k-和数对的最大数目.py
"""
#
# @lc app=leetcode.cn id=1679 lang=python3
#
# [1679] K 和数对的最大数目
#

from collections import defaultdict
# @lc code=start
from typing import List

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        print(counts)
        count = 0
        for i in counts:
            if k - i in counts:
                count += min(counts[i], counts[k - i])
        return count // 2
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.maxOperations([1, 2, 3, 4], 5))
    print(s.maxOperations([3, 1, 3, 4, 3], 6))
