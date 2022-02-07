#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-02-07 23:03:23
LastEditTime: 2022-02-07 23:06:25
Description: 
FilePath: 933.最近的请求次数.py
'''
#
# @lc app=leetcode.cn id=933 lang=python3
#
# [933] 最近的请求次数
#

# @lc code=start
class RecentCounter:

    def __init__(self):
        self.lst = []


    def ping(self, t: int) -> int:
        self.lst.append(t)






# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
# @lc code=end

