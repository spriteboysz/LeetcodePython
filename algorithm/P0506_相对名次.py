#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-15 22:29:55
LastEditTime: 2022-01-15 22:46:56
Description: 
FilePath: 506.相对名次.py
'''
#
# @lc app=leetcode.cn id=506 lang=python3
#
# [506] 相对名次
#

# @lc code=start
from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sort = sorted(score, reverse=True)
        rank = []
        for item in score:
            rank.append(sort.index(item) + 1)
        for i, v in enumerate(rank):
            if v == 1:
                rank[i] = "Gold Medal"
            elif v == 2:
                rank[i] = "Silver Medal"
            elif v == 3:
                rank[i] = "Bronze Medal"
            else:
                rank[i] = str(v)
        return rank


# @lc code=end
if __name__ == '__main__':
    s = Solution()
    print(s.findRelativeRanks([5, 4, 3, 2, 1]))
