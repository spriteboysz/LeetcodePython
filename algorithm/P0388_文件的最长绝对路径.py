#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-18 20:44:23
LastEditTime: 2022-03-18 22:12:51
Description: 
FilePath: 388.文件的最长绝对路径.py
"""
#
# @lc app=leetcode.cn id=388 lang=python3
#
# [388] 文件的最长绝对路径
#

# @lc code=start


class Solution:
    def lengthLongestPath(self, input: str) -> int:
        stack, files = [], []
        for item in input.split("\n"):
            index = item.count("\t")
            stack = stack[:index]
            item = item.replace("\t", "")
            if "." in item:
                path = "?".join(stack) + "?" if index else ""
                files.append(path + item)
            else:
                stack.append(item)

        return 0 if not files else max(map(len, files))


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.lengthLongestPath("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext")
    print(ans)
    ans = solution.lengthLongestPath(
        "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
    )
    print(ans)
    ans = solution.lengthLongestPath("a")
    print(ans)
    ans = solution.lengthLongestPath("file1.txt\nfile2.txt\nlongfile.txt")
    print(ans)
