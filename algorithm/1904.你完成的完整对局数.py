#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-10 22:50:41
LastEditTime: 2022-03-10 22:58:42
Description: 
FilePath: 1904.你完成的完整对局数.py
"""
#
# @lc app=leetcode.cn id=1904 lang=python3
#
# [1904] 你完成的完整对局数
#

# @lc code=start
from math import ceil, floor


class Solution:
    def numberOfRounds(self, loginTime: str, logoutTime: str) -> int:
        login_hh, login_mm = map(int, loginTime.split(":"))
        logout_hh, logout_mm = map(int, logoutTime.split(":"))
        login = 60 * login_hh + login_mm
        logout = 60 * logout_hh + logout_mm
        logout += 24 * 60 * int(login > logout)
        login, logout = ceil(login / 15), floor(logout / 15)
        return max(0, logout - login)


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.numberOfRounds("12:01", "12:44")
    print(ans)
    ans = solution.numberOfRounds("20:00", "06:00")
    print(ans)
