#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-13 23:40
LastEditTime: 2022-06-13 23:40
Description:
FilePath: 1006.笨阶乘.py
"""


class Solution:
    def clumsy(self, n: int) -> int:
        operator, stack = 0, [n]
        for i in range(n - 1, 0, -1):
            if operator == 0:
                stack.append(stack.pop() * i)
            if operator == 1:
                stack.append(int(stack.pop() / i))
            if operator == 2:
                stack.append(i)
            if operator == 3:
                stack.append(-i)
            operator = (operator + 1) % 4
        return sum(stack)


if __name__ == '__main__':
    solution = Solution()
    ans = solution.clumsy(4)
    print(ans)
    ans = solution.clumsy(10)
    print(ans)
