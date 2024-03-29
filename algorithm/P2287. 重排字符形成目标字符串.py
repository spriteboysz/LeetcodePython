#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-04 10:02
LastEditTime: 2022-06-04 10:02
Description:
FilePath: 2287.重排字符形成目标字符串.py
"""

from collections import defaultdict


class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        count1, count2 = defaultdict(int), defaultdict(int)
        for item in s:
            count1[item] += 1
        for item in target:
            count2[item] += 1

        count = len(s)
        for k, v in count2.items():
            count = min(count, count1[k] // v)
        return count


if __name__ == '__main__':
    solution = Solution()
    ans = solution.rearrangeCharacters(s="ilovecodingonleetcode", target="code")
    print(ans)
    ans = solution.rearrangeCharacters(s="abcba", target="abc")
    print(ans)
    ans = solution.rearrangeCharacters(s="abbaccaddaeea", target="aaaaa")
    print(ans)
