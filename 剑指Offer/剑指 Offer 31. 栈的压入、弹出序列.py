#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-20 22:41:54
LastEditTime: 2022-05-20 22:41:54
Description: 
FilePath: 剑指 Offer 31. 栈的压入、弹出序列.py
"""

from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack, popped = [], popped[::-1]
        for item in pushed:
            stack.append(item)
            while stack and popped and popped[-1] == stack[-1]:
                popped.pop()
                stack.pop()
        return stack == []


if __name__ == "__main__":
    solution = Solution()
    ans = solution.validateStackSequences(
        pushed=[1, 2, 3, 4, 5], popped=[4, 5, 3, 2, 1]
    )
    print(ans)
    ans = solution.validateStackSequences(
        pushed=[1, 2, 3, 4, 5], popped=[4, 3, 5, 1, 2]
    )
    print(ans)
