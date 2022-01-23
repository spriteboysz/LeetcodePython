#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-04 22:49:06
Description: 
FilePath: 1736.替换隐藏数字得到的最晚时间.py
'''
#
# @lc app=leetcode.cn id=1736 lang=python3
#
# [1736] 替换隐藏数字得到的最晚时间
#

# @lc code=start


class Solution:
    def maximumTime(self, time: str) -> str:
        maximum = ""
        for i, item in enumerate(time):
            if item == "?":
                if i == 0:
                    if time[1] != "?" and int(time[1]) >= 4:
                        maximum += "1"
                    else:
                        maximum += "2"
                if i == 1:
                    if maximum[0] == "0" or maximum[0] == "1":
                        maximum += "9"
                    else:
                        maximum += "3"
                if i == 3:
                    maximum += "5"
                if i == 4:
                    maximum += "9"
            else:
                maximum += item
        return maximum


# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.maximumTime("?0:15"))
