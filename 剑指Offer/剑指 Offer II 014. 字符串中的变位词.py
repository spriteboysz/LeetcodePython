#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-04 17:24
LastEditTime: 2022-06-04 17:24
Description:
FilePath: 剑指 Offer II 014. 字符串中的变位词.py
"""

from string import ascii_lowercase as lowercase


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        arr1, arr2 = [0] * 26, [0] * 26
        if len(s1) > len(s2):
            return False
        for i in range(len(s1)):
            arr1[lowercase.index(s1[i])] += 1
            arr2[lowercase.index(s2[i])] += 1

        for j in range(len(s1), len(s2)):
            if arr1 == arr2:
                return True
            arr2[lowercase.index(s2[j])] += 1
            arr2[lowercase.index(s2[j - len(s1)])] -= 1
        return arr1 == arr2


if __name__ == '__main__':
    solution = Solution()
    ans = solution.checkInclusion(s1="ab", s2="eidbaooo")
    print(ans)
