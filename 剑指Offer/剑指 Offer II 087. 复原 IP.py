#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-05 22:02
LastEditTime: 2022-06-05 22:02
Description:
FilePath: 剑指 Offer II 087. 复原 IP.py
"""

from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        if n < 4 or n > 12:
            return []

        def dfs(index, add):
            if len(add) > 4:
                return
            if index == n and len(add) == 4:
                addresses.append(add)
                return
            for i in range(index, n):
                temp = s[index:i + 1]
                if int(temp) < 256 and len(temp) == len(str(int(temp))):
                    dfs(i + 1, add + [temp])

        addresses = []
        dfs(0, [])
        return [".".join(add) for add in addresses]


if __name__ == '__main__':
    solution = Solution()
    ans = solution.restoreIpAddresses(s="25525511135")
    print(ans)
    ans = solution.restoreIpAddresses("0000")
    print(ans)
    ans = solution.restoreIpAddresses("010010")
    print(ans)
    ans = solution.restoreIpAddresses("10203040")
    print(ans)
