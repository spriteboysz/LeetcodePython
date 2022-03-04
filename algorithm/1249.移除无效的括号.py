#! /usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-03-05 00:02:52
LastEditTime: 2022-03-05 00:20:14
Description: 
FilePath: 1249.移除无效的括号.py
'''
#
# @lc app=leetcode.cn id=1249 lang=python3
#
# [1249] 移除无效的括号
#

# @lc code=start
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        count, valid = 0, ""
        for item in s:
            if item == "(":
                count += 1
            elif item == ")":
                count -= 1
            if count >= 0:
                valid += item
            else:
                count += 1
        if count == 0:
            return valid
        else:
            valid = valid[::-1].replace("(", "", count)
            return valid[::-1]
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.minRemoveToMakeValid("lee(t(c)o)de)")
    print(ans)
    ans = solution.minRemoveToMakeValid("a)b(c)d")
    print(ans)
    ans = solution.minRemoveToMakeValid("))((")
    print(ans)

