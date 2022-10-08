#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-02-12 14:25:24
LastEditTime: 2022-02-12 15:14:30
Description: 
FilePath: 640.求解方程.py
'''
#
# @lc app=leetcode.cn id=640 lang=python3
#
# [640] 求解方程
#

# @lc code=start


class Solution:
    def solveEquation(self, equation: str) -> str:
        left, right = equation.strip().split("=")
        left = left.strip().replace("-", "+-").lstrip("+").split("+")
        right = right.strip().replace("-", "+-").lstrip("+").split("+")
        for i in range(len(right) - 1, -1, -1):
            if "x" in right[i]:
                left.append(("-" + right.pop(i)).replace("--", ""))
        for i in range(len(left) - 1, -1, -1):
            if "x" not in left[i]:
                right.append(int(("-" + left.pop(i)).replace("--", "")))

        for i in range(len(left)):
            if left[i] == "x" or left[i] == "-x":
                left[i] = int(left[i].replace("x", "1"))
            else:
                left[i] = int(left[i].replace("x", ""))
        left, right = sum(map(int, left)), sum(map(int, right))
        if left == 0:
            return "No solution" if right else "Infinite solutions"
        else:
            return "x=" + str(right//left)
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.solveEquation(equation="x+5-3+x=6+x-2"))
    print(s.solveEquation("x=x"))
    print(s.solveEquation("2x=x"))
    print(s.solveEquation("x=x+2"))
    print(s.solveEquation("2=-x"))
    print(s.solveEquation("2+2-x+x+3x=x+2x-x+x+4"))
