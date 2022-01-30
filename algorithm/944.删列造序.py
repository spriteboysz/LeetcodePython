#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-30 23:53:28
LastEditTime: 2022-01-30 23:59:47
Description: 
FilePath: 944.删列造序.py
'''
#
# @lc app=leetcode.cn id=944 lang=python3
#
# [944] 删列造序
#

# @lc code=start
from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        for item in zip(*list(map(list, strs))):
            if sorted(list(item)) != list(item):
                count += 1
        return count
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.minDeletionSize(strs=["cba", "daf", "ghi"]))
    print(s.minDeletionSize(["a", "b"]))
    print(s.minDeletionSize(["zyx", "wvu", "tsr"]))
