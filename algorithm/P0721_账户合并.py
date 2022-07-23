#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-17 12:09:07
LastEditTime: 2022-04-17 12:11:35
Description: 
FilePath: 721.账户合并.py
"""
#
# @lc app=leetcode.cn id=721 lang=python3
#
# [721] 账户合并
#

from collections import defaultdict
# @lc code=start
from typing import List

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emailuser = defaultdict(str)
        for account in accounts:
            user, *emails = account
            # print(user, emails)
            for email in emails:
                for m, u in emailuser.items():
                    if email in m:
                        key = list(m) + emails
                        emailuser[tuple(key)] = u
                        emailuser[m] = None
                        break
                else:
                    emailuser[tuple(emails)] = user
        result = []
        for k, v in emailuser.items():
            if v:
                result.append([v, ",".join(sorted(set(k)))])
        return result


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.accountsMerge(
        accounts=[
            ["John", "johnsmith@mail.com", "john00@mail.com"],
            ["John", "johnnybravo@mail.com"],
            ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
            ["Mary", "mary@mail.com"],
        ]
    )
    print(ans)
