#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-10 22:33:46
LastEditTime: 2022-02-10 22:45:23
Description:
FilePath: 299.猜数字游戏.py
"""
#
# @lc app=leetcode.cn id=299 lang=python3
#
# [299] 猜数字游戏
#

# @lc code=start


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        sec, gue = [], []
        bulls, cows = 0, 0
        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                sec.append(s)
                gue.append(g)
        for i in range(10):
            cows += min(sec.count(str(i)), gue.count(str(i)))
        return "{}A{}B".format(bulls, cows)

# @lc code=end


if __name__ == "__main__":
    s = Solution()
    #print(s.getHint("1123", "0111"))
    print(s.getHint("0194", "9038"))
