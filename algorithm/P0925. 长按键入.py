#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-02 22:53:55
LastEditTime: 2022-02-02 23:07:51
Description:
FilePath: 925.长按键入.py
"""
#
# @lc app=leetcode.cn id=925 lang=python3
#
# [925] 长按键入
#

# @lc code=start


class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i, j = 0, 0
        for i in range(len(typed)):
            if j < len(name) and typed[i] == name[j]:
                i += 1
                j += 1
            elif i > 0 and typed[i] == name[j - 1]:
                i += 1
            else:
                return False
        return True if j == len(name) else False


# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.isLongPressedName("alex", "aaleex"))
    print(s.isLongPressedName("saeed", "ssaaedd"))
    print(s.isLongPressedName("leelee", "lleeelee"))
    print(s.isLongPressedName("laiden", "laiden"))
    print(s.isLongPressedName("vtkgn", "vttkgnn"))
