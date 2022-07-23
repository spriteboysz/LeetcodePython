#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-12 22:12:42
LastEditTime: 2022-03-12 22:37:26
Description: 
FilePath: 1743.从相邻元素对还原数组.py
"""
#
# @lc app=leetcode.cn id=1743 lang=python3
#
# [1743] 从相邻元素对还原数组
#

from collections import defaultdict
# @lc code=start
from typing import List

class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for pair in adjacentPairs:
            adj[pair[0]].append(pair[1])
            adj[pair[1]].append(pair[0])

        head = min(adj.items(), key=lambda el: len(el[1]))
        array, cur = [head[0]], head[1][0]
        while True:
            array.append(cur)
            if len(array) > len(adjacentPairs):
                break
            adj[cur].remove(array[-2])
            cur = adj[cur][0]
        return array


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.restoreArray([[2, 1], [3, 4], [3, 2]])
    print(ans)
    ans = solution.restoreArray([[4, -2], [1, 4], [-3, 1]])
    print(ans)
    ans = solution.restoreArray([[100000, -100000]])
    print(ans)
