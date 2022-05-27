#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-27 22:43
LastEditTime: 2022-05-27 22:43
Description:
FilePath: 2255.统计是给定字符串前缀的字符串数目.py
"""

from typing import List


class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        return sum([1 for word in words if s.startswith(word)])
        # count = 0
        # for word in words:
        #     if s.startswith(word):
        #         count += 1
        # return count


if __name__ == '__main__':
    solution = Solution()
    ans = solution.countPrefixes(["a", "a"], "aa")
    print(ans)
