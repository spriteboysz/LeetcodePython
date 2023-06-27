#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-06 22:33:53
LastEditTime: 2022-03-06 22:43:40
Description: 
FilePath: 1481.不同整数的最少数目.py
"""
#
# @lc app=leetcode.cn id=1481 lang=python3
#
# [1481] 不同整数的最少数目
#

from collections import defaultdict
# @lc code=start
from typing import List


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counts = defaultdict(int)
        for item in arr:
            counts[item] += 1
        # print(list(counts.items()))
        for i, item in enumerate(sorted(list(counts.items()), key=lambda el: el[1])):
            if k - item[1] < 0:
                return len(counts) - i
            k -= item[1]
        return 0


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.findLeastNumOfUniqueInts([5, 5, 4], 1)
    print(ans)
    ans = solution.findLeastNumOfUniqueInts([4, 3, 1, 1, 3, 3, 2], 3)
    print(ans)
