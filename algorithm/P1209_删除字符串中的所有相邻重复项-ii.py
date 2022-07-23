#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-04 23:13:50
LastEditTime: 2022-03-04 23:22:33
Description: 
FilePath: 1209.删除字符串中的所有相邻重复项-ii.py
"""
#
# @lc app=leetcode.cn id=1209 lang=python3
#
# [1209] 删除字符串中的所有相邻重复项 II
#

# @lc code=start
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for letter in s:
            if not stack or stack[-1][0] != letter:
                stack.append([letter, 1])
            elif stack[-1][1] + 1 < k:
                stack[-1][1] += 1
            else:
                stack.pop()

        return "".join([letter * count for letter, count in stack])


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.removeDuplicates("abcd", 2)
    print(ans)
    ans = solution.removeDuplicates("deeedbbcccbdaa", 3)
    print(ans)
    ans = solution.removeDuplicates("pbbcggttciiippooaais", 2)
    print(ans)
