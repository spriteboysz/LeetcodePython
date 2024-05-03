#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-05-02 20:09
FileName: LCP
Description:LCR 086. 分割回文串.py 
"""
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def backtrack(i, start):
            if i == n:
                paths.append(path.copy())
                return
            if i < n - 1:
                backtrack(i + 1, start)
            ss = s[start:i + 1]
            if ss == ss[::-1]:
                path.append(ss)
                backtrack(i + 1, i + 1)
                path.pop()

        paths, path, n = [], [], len(s)
        backtrack(0, 0)
        return paths


if __name__ == '__main__':
    print(Solution().partition(s="eeee"))
