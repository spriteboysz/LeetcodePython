#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-26 23:30:24
LastEditTime: 2022-01-26 23:35:06
Description: 
FilePath: 1323.6-和-9-组成的最大数字.py
'''
#
# @lc app=leetcode.cn id=1323 lang=python3
#
# [1323] 6 和 9 组成的最大数字
#

# @lc code=start
class Solution:
    def maximum69Number(self, num: int) -> int:
        num2 = ""
        flag = True
        for item in str(num):
            if flag and item == "6":
                num2 += "9"
                flag = False
            else:
                num2 += item
        return int(num2)

# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.maximum69Number(9669))
    print(s.maximum69Number(9996))
    print(s.maximum69Number(9999))
