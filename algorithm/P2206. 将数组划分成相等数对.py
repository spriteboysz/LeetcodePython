#! /usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-03-30 22:21:46
LastEditTime: 2022-03-30 22:24:56
Description: 
FilePath: 2206.将数组划分成相等数对.py
'''
#
# @lc app=leetcode.cn id=2206 lang=python3
#
# [2206] 将数组划分成相等数对
#

from collections import defaultdict
# @lc code=start
from typing import List

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        numcount = defaultdict(int)
        for num in nums:
            numcount[num] += 1
        for v in numcount.values():
            if v % 2 == 1:
                return False
        return True


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.divideArray([3, 2, 3, 2, 2, 2])
    print(ans)
    ans = solution.divideArray([1, 2, 3, 4])
    print(ans)
