#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-16 23:11
LastEditTime: 2022-06-16 23:11
Description:
FilePath: 131.分割回文串.py
"""

from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def dfs(s, path):
            if not s:
                res.append(path)
            for i in range(1, len(s) + 1):
                if s[:i] == s[:i][::-1]:
                    dfs(s[i:], path + [s[:i]])

        res = []
        dfs(s, [])
        return res


if __name__ == '__main__':
    solution = Solution()
    ans = solution.partition("aab")
    print(ans)
