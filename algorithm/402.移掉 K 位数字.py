#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-28 22:50
LastEditTime: 2022-05-28 22:50
Description:
FilePath: 402.移掉 K 位数字.py
"""


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for n in num:
            while k and stack and stack[-1] > n:
                k -= 1
                stack.pop()
            stack.append(n)
        return "".join(stack[:len(stack) - k]).lstrip("0") or "0"


if __name__ == '__main__':
    solution = Solution()
    ans = solution.removeKdigits(num="1432219", k=3)
    print(ans)
