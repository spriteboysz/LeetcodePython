#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-05 16:07:25
Description: 
FilePath: 485.最大连续-1-的个数.py
'''
#
# @lc app=leetcode.cn id=485 lang=python3
#
# [485] 最大连续 1 的个数
#

# @lc code=start
from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        lst = "".join(list(map(str, nums))).split("0")
        return max(list(map(len, lst)))
    
# @lc code=end

if __name__ == '__main__':
    s = Solution()
    r = s.findMaxConsecutiveOnes([1,1,0,1,1,1])
    print(r)
    

