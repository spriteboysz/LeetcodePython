#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-20 23:47:28
LastEditTime: 2022-01-20 23:54:18
Description: 
FilePath: 1018.可被-5-整除的二进制前缀.py
'''
#
# @lc app=leetcode.cn id=1018 lang=python3
#
# [1018] 可被 5 整除的二进制前缀
#

# @lc code=start
from typing import List


class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        answer, current = [], 0
        for item in nums:
            current = 2 * current + item
            answer.append(current % 5 == 0)
        return answer

# @lc code=end


if __name__ == '__main__':
    s = Solution()
    print(s.prefixesDivBy5([1, 1, 1]))
    print(s.prefixesDivBy5([0, 1, 1, 1, 1, 1]))
    print(s.prefixesDivBy5([1, 1, 1, 0, 1]))
