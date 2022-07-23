#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-17 22:44
LastEditTime: 2022-06-17 22:44
Description:
FilePath: 1358.包含所有三种字符的子字符串数目.py
"""


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count_char = {'a': 0, 'b': 0, 'c': 0}
        count = 0
        for i, c in enumerate(s):
            count_char[c] = i + 1
            count += min(count_char['a'], count_char['b'], count_char['c'])
        return count


if __name__ == '__main__':
    solution = Solution()
    ans = solution.numberOfSubstrings("abcabc")
    print(ans)
    ans = solution.numberOfSubstrings("aaacb")
    print(ans)
