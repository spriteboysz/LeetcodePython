#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-28 00:12:30
LastEditTime: 2022-01-28 00:16:10
Description:
FilePath: 1221.分割平衡字符串.py
"""
#
# @lc app=leetcode.cn id=1221 lang=python3
#
# [1221] 分割平衡字符串
#

# @lc code=start


class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count, height = 0, 0
        for item in s:
            if item == "R":
                height += 1
            elif item == "L":
                height -= 1
            if height == 0:
                count += 1
        return count
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.balancedStringSplit("RLRRLLRLRL"))
    print(s.balancedStringSplit("RLLLLRRRLR"))
    print(s.balancedStringSplit("LLLLRRRR"))
    print(s.balancedStringSplit("RLRRRLLRLL"))
