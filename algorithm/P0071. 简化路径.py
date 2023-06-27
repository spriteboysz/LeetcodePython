#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-26 15:40:41
LastEditTime: 2022-02-26 15:47:25
Description: 
FilePath: 71.简化路径.py
"""


#
# @lc app=leetcode.cn id=71 lang=python3
#
# [71] 简化路径
#

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        directories = path.replace("//", "/").split("/")
        stack = []
        for directory in filter(lambda el: el != "", directories):
            if len(stack) != 0 and directory == "..":
                stack.pop()
            elif directory == "." or directory == "..":
                pass
            else:
                stack.append(directory)
        return "/" + "/".join(stack)


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.simplifyPath("/home/")
    print(ans)
    ans = solution.simplifyPath("/../")
    print(ans)
    ans = solution.simplifyPath("/home//foo/")
    print(ans)
    ans = solution.simplifyPath("/a/./b/../../c/")
    print(ans)
