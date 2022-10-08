#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-14 23:13
LastEditTime: 2022-06-14 23:13
Description:
FilePath: 2299.强密码检验器 II.py
"""
"""
它有至少8个字符。
至少包含 一个小写英文字母。
至少包含 一个大写英文字母。
至少包含 一个数字。
至少包含 一个特殊字符。特殊字符为："!@#$%^&*()-+"中的一个。
它不包含2个连续相同的字符（比方说"aab"不符合该条件，但是"aba"符合该条件）。
"""


class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password) < 8:
            return False
        flag1, flag2, flag3, flag4 = False, False, False, False
        for i, c in enumerate(password):
            if c.isdigit():
                flag1 = True
            if c.islower():
                flag2 = True
            if c.isupper():
                flag3 = True
            if c in "!@#$%^&*()-+":
                flag4 = True
            if i != 0 and c == password[i - 1]:
                return False
        return flag1 and flag2 and flag3 and flag4


if __name__ == '__main__':
    solution = Solution()
    ans = solution.strongPasswordCheckerII(password="IloveLe3tcode!")
    print(ans)
    ans = solution.strongPasswordCheckerII(password="Me+You--IsMyDream")
    print(ans)
    ans = solution.strongPasswordCheckerII(password="1aB!")
    print(ans)
