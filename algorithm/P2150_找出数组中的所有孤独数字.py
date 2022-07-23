#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-02-08 23:25:45
LastEditTime: 2022-02-08 23:33:49
Description:
FilePath: 2150.找出数组中的所有孤独数字.py
'''
#
# @lc app=leetcode.cn id=2150 lang=python3
#
# [2150] 找出数组中的所有孤独数字
#

# @lc code=start
from typing import List


class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        count = dict()
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        lonely = []
        for num in count:
            if count[num] == 1:
                if num - 1 not in count and num + 1 not in count:
                    lonely.append(num)
        return lonely
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.findLonely([1, 3, 5, 3]))
    print(s.findLonely([10, 6, 5, 8]))
