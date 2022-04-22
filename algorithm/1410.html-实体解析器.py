#! /usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-04-22 23:03:04
LastEditTime: 2022-04-22 23:14:34
Description: 
FilePath: 1410.html-实体解析器.py
'''
#
# @lc app=leetcode.cn id=1410 lang=python3
#
# [1410] HTML 实体解析器
#

# @lc code=start
class Solution:
    def entityParser(self, text: str) -> str:
        dic = {
            "&quot;": '"',
            "&apos;": "'",
            "&gt;": ">",
            "&lt;": "<",
            "&frasl;": "/",
            "&amp;": "&",
        }
        for k, v in dic.items():
            text = text.replace(k, v)
        return text


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.entityParser(text="&amp; is an HTML entity but &ambassador; is not.")
    print(ans)
    ans = solution.entityParser(text = "and I quote: &quot;...&quot;")
    print(ans)
