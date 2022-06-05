#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-05 13:45
LastEditTime: 2022-06-05 13:45
Description:
FilePath: 剑指 Offer 67. 把字符串转换成整数.py
"""


class Solution:
    def strToInt(self, str: str) -> int:
        str = str.strip()
        if not str:
            return 0
        integer, index, sign = 0, 1, 1
        int_max, int_min, bndry = 2 ** 31 - 1, -2 ** 31, 2 ** 31 // 10
        if str[0] == "-":
            sign = -1  # 保存负号
        elif str[0] != "+":
            index = 0  # 若无符号位，则需从 i = 0 开始数字拼接
        for c in str[index:]:
            if not "0" <= c <= "9":
                break  # 遇到非数字的字符则跳出
            if integer > bndry or integer == bndry and c > "7":
                return int_max if sign == 1 else int_min  # 数字越界处理
            integer = 10 * integer + ord(c) - ord("0")  # 数字拼接
        return sign * integer


if __name__ == '__main__':
    solution = Solution()
    ans = solution.strToInt("   -42")
    print(ans)
