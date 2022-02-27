#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-27 09:52:13
LastEditTime: 2022-02-27 10:00:20
Description: 
FilePath: 831.隐藏个人信息.py
"""
#
# @lc app=leetcode.cn id=831 lang=python3
#
# [831] 隐藏个人信息
#

# @lc code=start
from concurrent.futures.process import _python_exit


class Solution:
    def maskPII(self, s: str) -> str:
        if "@" in s:
            name, domain = s.lower().split("@")
            return name[0] + "*" * 5 + name[-1] + "@" + domain

        else:
            phone = "".join([num for num in s if num.isdigit()])
            mod = len(phone) % 10
            prefix = "+" * int(mod != 0) + "*" * mod + "-" + "***-" * 2
            return prefix.lstrip("-") + phone[-4:]


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.maskPII("LeetCode@LeetCode.com")
    print(ans)
    ans = solution.maskPII("AB@qq.com")
    print(ans)
    ans = solution.maskPII("1(234)567-890")
    print(ans)
    ans = solution.maskPII("86-(10)12345678")
    print(ans)
