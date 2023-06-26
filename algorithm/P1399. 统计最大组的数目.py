#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-26 00:00:43
LastEditTime: 2022-01-26 00:08:25
Description:
FilePath: 1399.统计最大组的数目.py
"""
#
# @lc app=leetcode.cn id=1399 lang=python3
#
# [1399] 统计最大组的数目
#

# @lc code=start


class Solution:
    def countLargestGroup(self, n: int) -> int:
        counter = [0] * 50
        for i in range(1, n + 1):
            counter[sum(map(int, list(str(i))))] += 1
        return counter.count(max(counter))

# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.countLargestGroup(13))
    print(s.countLargestGroup(2))
    print(s.countLargestGroup(15))
    print(s.countLargestGroup(24))
