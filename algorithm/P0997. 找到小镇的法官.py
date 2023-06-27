#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-19 23:49:39
LastEditTime: 2022-01-20 00:12:00
Description:
FilePath: 997.找到小镇的法官.py
"""
#
# @lc app=leetcode.cn id=997 lang=python3
#
# [997] 找到小镇的法官
#

# @lc code=start
from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        judge = {}
        for item in trust:
            if item[1] in judge.keys():
                judge[item[1]].append(item[0])
            else:
                judge[item[1]] = [item[0]]

        la, lb = [], []
        for k, v in judge.items():
            if len(v) == n - 1:
                la.append(k)
            lb.extend(v)

        for item in la:
            if item not in lb:
                return item

        return 1 if n == 1 else -1


# @lc code=end

if __name__ == '__main__':
    s = Solution()
    print(s.findJudge(3, [[1, 2], [2, 3]]))
