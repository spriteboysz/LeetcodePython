#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-10 23:58:35
LastEditTime: 2022-01-11 00:04:47
Description:
FilePath: 165.比较版本号.py
"""
#
# @lc app=leetcode.cn id=165 lang=python3
#
# [165] 比较版本号
#

# @lc code=start
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1, v2 = list(version1.split(".")), list(version2.split("."))
        if len(v1) < len(v2):
            v1.extend([0] * (len(v2) - len(v1)))
        else:
            v2.extend([0] * (len(v1) - len(v2)))
        for i, j in zip(v1, v2):
            if int(i) > int(j):
                return 1
            elif int(i) < int(j):
                return -1
        else:
            return 0

            
# @lc code=end

if __name__ == '__main__':
    s = Solution()
    print(s.compareVersion("7.5.2.4", "7.5.3"))
    