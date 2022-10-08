#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-02-12 15:17:04
LastEditTime: 2022-02-12 15:29:56
Description: 
FilePath: 2155.分组得分最高的所有下标.py
'''
#
# @lc app=leetcode.cn id=2155 lang=python3
#
# [2155] 分组得分最高的所有下标
#

# @lc code=start
from typing import List


class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        left, right = 0, nums.count(1)
        score = [(0, left + right)]
        for i in range(0, len(nums)):
            if nums[i] == 0:
                left += 1
            elif nums[i] == 1:
                right -= 1
            score.append((i + 1, left + right))
        maximum = max(map(lambda el: el[1], score))
        return [i for i, v in score if v == maximum]

# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.maxScoreIndices([0, 0, 1, 0]))
    print(s.maxScoreIndices([0, 0, 0]))
    print(s.maxScoreIndices([1, 1]))
