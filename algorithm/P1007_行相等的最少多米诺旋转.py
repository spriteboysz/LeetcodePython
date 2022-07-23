#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-16 19:44:07
LastEditTime: 2022-03-16 19:52:03
Description: 
FilePath: 1007.行相等的最少多米诺旋转.py
"""
#
# @lc app=leetcode.cn id=1007 lang=python3
#
# [1007] 行相等的最少多米诺旋转
#

# @lc code=start
from typing import List

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        if tops[0] in [tops[1], bottoms[1]]:
            common = tops[0]
        elif tops[1] in [tops[1], bottoms[1]]:
            common = tops[1]
        else:
            return -1
            
        top_common, bottom_common = 0, 0
        for a, b in zip(tops, bottoms):
            if a != common and b != common:
                return -1
            if a == common:
                top_common += 1
            if b == common:
                bottom_common += 1
        return min(len(tops) - top_common, len(bottoms) - bottom_common)


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    # ans = solution.minDominoRotations([2, 1, 2, 4, 2, 2], [5, 2, 6, 2, 3, 2])
    # print(ans)
    # ans = solution.minDominoRotations([3, 5, 1, 2, 3], [3, 6, 3, 3, 4])
    # print(ans)
    ans = solution.minDominoRotations(
        [1, 2, 1, 1, 1, 2, 2, 2], [2, 1, 2, 2, 2, 2, 2, 2]
    )
    print(ans)
