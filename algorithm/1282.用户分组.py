#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-02-15 22:07:14
LastEditTime: 2022-02-15 22:19:29
Description: 
FilePath: 1282.用户分组.py
'''
#
# @lc app=leetcode.cn id=1282 lang=python3
#
# [1282] 用户分组
#

# @lc code=start
from typing import List
from collections import defaultdict


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groupindex = defaultdict(list)
        for i, v in enumerate(groupSizes):
            groupindex[v].append(i)
        groups = []
        for k, v in groupindex.items():
            for i in range(0, len(v), k):
                groups.append(v[i:i+k])
        return groups

# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.groupThePeople([3, 3, 3, 3, 3, 1, 3]))
    print(s.groupThePeople([2, 1, 3, 3, 3, 2]))
