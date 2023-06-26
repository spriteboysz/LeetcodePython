#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-26 23:38:07
LastEditTime: 2022-01-26 23:41:08
Description:
FilePath: 1313.解压缩编码列表.py
"""
#
# @lc app=leetcode.cn id=1313 lang=python3
#
# [1313] 解压缩编码列表
#

# @lc code=start
from typing import List


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        decompress = []
        for i in range(0, len(nums), 2):
            decompress.extend([nums[i + 1]] * nums[i])
        return decompress
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.decompressRLElist([1, 1, 2, 3]))
