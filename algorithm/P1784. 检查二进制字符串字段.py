#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-23 17:29:25
LastEditTime: 2022-01-23 17:40:48
Description:
FilePath: 1784.检查二进制字符串字段.py
"""
#
# @lc app=leetcode.cn id=1784 lang=python3
#
# [1784] 检查二进制字符串字段
#

# @lc code=start


class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        count = [1] * len(s)
        for i in range(1, len(s)):
            if s[i - 1] == s[i] == "1":
                count[i] = count[i - 1] + 1
                count[i - 1] = 0
            elif s[i] == "0":
                count[i] = 0
        return len(list(filter(lambda el: el >= 1, count))) == 1
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.checkOnesSegment("1"))
    print(s.checkOnesSegment("10"))
