#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-28 22:04:58
LastEditTime: 2022-01-28 22:23:41
Description: 
FilePath: 1047.删除字符串中的所有相邻重复项.py
'''
#
# @lc app=leetcode.cn id=1047 lang=python3
#
# [1047] 删除字符串中的所有相邻重复项
#

# @lc code=start


class Solution:
    def removeDuplicates(self, s: str) -> str:
        s = list(s)
        while True:
            for i in range(len(s) - 1):
                if s[i] == s[i + 1]:
                    s.pop(i + 1)
                    s.pop(i)
                    break
            else:
                break
        return "".join(s)
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.removeDuplicates("aababaab"))