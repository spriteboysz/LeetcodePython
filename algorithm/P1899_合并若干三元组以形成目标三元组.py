#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-13 23:16:31
LastEditTime: 2022-03-13 23:32:28
Description: 
FilePath: 1899.合并若干三元组以形成目标三元组.py
"""
#
# @lc app=leetcode.cn id=1899 lang=python3
#
# [1899] 合并若干三元组以形成目标三元组
#

# @lc code=start
from typing import List


class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        flag0, flag1, flag2 = False, False, False
        for triplet in triplets:
            if (
                triplet[0] > target[0]
                or triplet[1] > target[1]
                or triplet[2] > target[2]
            ):
                continue
            if triplet[0] == target[0]:
                flag0 = True
            if triplet[1] == target[1]:
                flag1 = True
            if triplet[2] == target[2]:
                flag2 = True

            if flag0 and flag1 and flag2:
                return True
        return False


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.mergeTriplets(
        triplets=[[2, 5, 3], [1, 8, 4], [1, 7, 5]], target=[2, 7, 5]
    )
    print(ans)
    ans = solution.mergeTriplets(triplets=[[1, 3, 4], [2, 5, 8]], target=[2, 5, 8])
    print(ans)
    ans = solution.mergeTriplets(
        triplets=[[2, 5, 3], [2, 3, 4], [1, 2, 5], [5, 2, 3]], target=[5, 5, 5]
    )
    print(ans)
    ans = solution.mergeTriplets(triplets=[[3, 4, 5], [4, 5, 6]], target=[3, 2, 5])
    print(ans)
