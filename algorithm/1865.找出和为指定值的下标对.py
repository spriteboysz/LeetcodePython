#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-02-12 15:42:08
LastEditTime: 2022-02-12 15:56:29
Description: 
FilePath: 1865.找出和为指定值的下标对.py
'''
#
# @lc app=leetcode.cn id=1865 lang=python3
#
# [1865] 找出和为指定值的下标对
#

# @lc code=start
from typing import List
from collections import Counter


class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums2 = nums2
        self.dict1 = Counter(nums1)
        self.dict2 = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        temp = self.nums2[index]
        self.nums2[index] += val
        self.dict2[temp] -= 1
        self.dict2[temp + val] += 1

    def count(self, tot: int) -> int:
        count = 0
        for k, v in self.dict1.items():
            count += v * self.dict2.get(tot - k, 0)
        return count


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)
# @lc code=end
