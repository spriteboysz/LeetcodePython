#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-19 23:41:38
LastEditTime: 2022-02-19 23:54:19
Description: 
FilePath: 394.字符串解码.py
"""
#
# @lc app=leetcode.cn id=394 lang=python3
#
# [394] 字符串解码
#

# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        decode = ""
        for item in s:
            if item.isdigit():
                if stack == [] or not stack[-1].isdigit():
                    stack.append(int(item))
                else:
                    stack[-1] = 10 * stack[-1] + int(item)
            elif item == "[":
                stack.append(item)
            elif item.islower():
                if stack == [] or not stack[-1].islower():
                    stack.append(item)
                else:
                    stack[-1] += item
            elif item == "]":
                word = stack.pop()
                stack.pop()
                count = stack.pop()
                print(word, count)
                word2 = word * count
                if stack != []:
                    stack.append(word2)
                else:
                    decode += word2
        return decode


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.decodeString("3[a]2[bc]")
    print(ans)
    ans2 = solution.decodeString("3[a2[c]]")
    print(ans2)
