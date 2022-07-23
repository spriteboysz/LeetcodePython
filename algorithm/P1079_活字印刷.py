#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-25 22:51:49
LastEditTime: 2022-02-25 22:55:48
Description: 
FilePath: 1079.活字印刷.py
"""
#
# @lc app=leetcode.cn id=1079 lang=python3
#
# [1079] 活字印刷
#

# @lc code=start
from itertools import permutations


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        sequence = set()
        for i in range(1, len(tiles) + 1):
            for item in permutations(tiles, i):
                sequence.add(item)
        return len(sequence)


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.numTilePossibilities("AAABBC")
    print(ans)
