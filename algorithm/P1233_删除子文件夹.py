#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-04 23:47:08
LastEditTime: 2022-03-04 23:51:43
Description: 
FilePath: 1233.删除子文件夹.py
"""
#
# @lc app=leetcode.cn id=1233 lang=python3
#
# [1233] 删除子文件夹
#

# @lc code=start
from typing import List


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        stack = []
        for f in sorted(folder):
            if not stack:
                stack.append(f)
            elif f.startswith(stack[-1]) and stack[-1].count("/") != f.count("/"):
                pass
            else:
                stack.append(f)
        return stack


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.removeSubfolders(["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"])
    print(ans)
    ans = solution.removeSubfolders(["/a", "/a/b/c", "/a/b/d"])
    print(ans)
    ans = solution.removeSubfolders(["/a/b/c", "/a/b/ca", "/a/b/d"])
    print(ans)
    ans = solution.removeSubfolders(["/c", "/d/c/e"])
    print(ans)
