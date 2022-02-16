#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-16 22:10:58
LastEditTime: 2022-02-16 22:16:48
Description: 
FilePath: 260.只出现一次的数字-iii.py
"""
#
# @lc app=leetcode.cn id=260 lang=python3
#
# [260] 只出现一次的数字 III
#

# @lc code=start
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        count = dict()
        for num in nums:
            if num in count:
                count.pop(num)
            else:
                count[num] = 1
        return list(count)


# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.singleNumber([1, 2, 1, 3, 2, 5]))
    print(s.singleNumber([-1, 0]))



