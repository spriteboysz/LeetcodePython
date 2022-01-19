#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-19 22:29:47
LastEditTime: 2022-01-19 22:48:17
Description: 
FilePath: 922.按奇偶排序数组-ii.py
'''
#
# @lc app=leetcode.cn id=922 lang=python3
#
# [922] 按奇偶排序数组 II
#

# @lc code=start
from typing import List


class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        odd, even, lst = [], [], []
        for item in nums:
            if item % 2 == 0:
                even.append(item)
            else:
                odd.append(item)

        for i in range(len(odd)):
            lst.append(even[i])
            lst.append(odd[i])
        return lst

# @lc code=end


if __name__ == '__main__':
    s = Solution()
    print(s.sortArrayByParityII([4, 2, 5, 7]))
