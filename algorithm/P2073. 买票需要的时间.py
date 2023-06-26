#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-01 22:12:46
LastEditTime: 2022-02-01 22:17:17
Description:
FilePath: 2073.买票需要的时间.py
"""
#
# @lc app=leetcode.cn id=2073 lang=python3
#
# [2073] 买票需要的时间
#

# @lc code=start
from typing import List


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        count = 0
        for i in range(len(tickets)):
            if i <= k:
                count += min(tickets[i], tickets[k])
            else:
                count += min(tickets[i], tickets[k]-1)
        return count

# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.timeRequiredToBuy([5, 1, 1, 1], 0))
