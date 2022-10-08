#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-26 16:16:29
LastEditTime: 2022-02-26 16:33:56
Description: 
FilePath: 722.删除注释.py
"""
#
# @lc app=leetcode.cn id=722 lang=python3
#
# [722] 删除注释
#

# @lc code=start
from typing import List


class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        s = "\n".join(source) + "\n"
        i, code = 1, ""
        while i < len(s):
            if s[i - 1] + s[i] == "//":
                i = s.find("\n", i) + 1
            elif s[i - 1] + s[i] == "/*":
                i = s.find("*/", i + 1) + 3
            else:
                code += s[i - 1]
                i += 1
        return list(filter(len, code.split("\n")))


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.removeComments(
        [
            "/*Test program */",
            "int main()",
            "{ ",
            "  // variable declaration ",
            "int a, b, c;",
            "/* This is a test",
            "   multiline  ",
            "   comment for ",
            "   testing */",
            "a = b + c;",
            "}",
        ]
    )
    print(ans)
