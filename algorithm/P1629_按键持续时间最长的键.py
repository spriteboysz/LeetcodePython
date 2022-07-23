#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-30 22:50:26
LastEditTime: 2022-01-30 22:58:12
Description: 
FilePath: 1629.按键持续时间最长的键.py
'''
#
# @lc app=leetcode.cn id=1629 lang=python3
#
# [1629] 按键持续时间最长的键
#

# @lc code=start
from typing import List


class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        time = [releaseTimes[0]]
        for i in range(1, len(releaseTimes)):
            time.append(releaseTimes[i] - releaseTimes[i - 1])
        maximum = max(time)
        key = []
        for i, item in enumerate(time):
            if item == maximum:
                key.append(keysPressed[i])
        return max(key)

# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.slowestKey([9, 29, 49, 50], "cbcd"))
    print(s.slowestKey([12, 23, 36, 46, 62], "spuda"))
