#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-10 13:36:41
LastEditTime: 2022-04-10 13:42:19
Description: 
FilePath: 331.验证二叉树的前序序列化.py
"""
#
# @lc app=leetcode.cn id=331 lang=python3
#
# [331] 验证二叉树的前序序列化
#

# @lc code=start
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        stack = []
        for item in preorder.split(","):
            stack.append(item)
            while (
                len(stack) >= 3 and stack[-1] == stack[-2] == "#" and stack[-3] != "#"
            ):
                stack = stack[:-3]
                stack.append("#")
        return stack == ["#"]


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.isValidSerialization(preorder="9,3,4,#,#,1,#,#,2,#,6,#,#")
    print(ans)
    ans = solution.isValidSerialization("1, #")
    print(ans)
    ans = solution.isValidSerialization("9, #, #, 1")
    print(ans)
