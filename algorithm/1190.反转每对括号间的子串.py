#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-04 22:45:10
LastEditTime: 2022-03-04 22:50:15
Description: 
FilePath: 1190.反转每对括号间的子串.py
"""
#
# @lc app=leetcode.cn id=1190 lang=python3
#
# [1190] 反转每对括号间的子串
#

# @lc code=start
class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for item in s:
            if item != ")":
                stack.append(item)
            else:
                cur = []
                while stack[-1] != "(":
                    cur.append(stack.pop())
                stack.pop()
                stack.extend(cur)
        return "".join(stack)


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.reverseParentheses("(abcd)")
    print(ans)
    ans = solution.reverseParentheses("(u(love)i)")
    print(ans)
    ans = solution.reverseParentheses(s="(ed(et(oc))el)")
    print(ans)
    ans = solution.reverseParentheses(s="a(bcdefghijkl(mno)p)q")
    print(ans)
