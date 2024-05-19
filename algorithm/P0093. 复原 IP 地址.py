#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-05-19 16:56
FileName: algorithm
Description:P0093. 复原 IP 地址.py 
"""
from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def backtrack(i):
            if i == n and len(path) == 4:
                paths.append('.'.join(map(str, path.copy())))
            for j in range(i, n):
                session = s[i:j + 1]
                if str(int(session)) != session:
                    break
                if len(path) < 4 and 0 <= int(session) <= 255:
                    path.append(int(session))
                    backtrack(j + 1)
                    path.pop()

        n, path, paths = len(s), [], []
        backtrack(0)
        return paths


if __name__ == '__main__':
    print(Solution().restoreIpAddresses(s="101023"))
