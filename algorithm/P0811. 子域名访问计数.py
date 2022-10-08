#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-28 22:44:04
LastEditTime: 2022-02-28 22:47:38
Description: 
FilePath: 811.子域名访问计数.py
"""
#
# @lc app=leetcode.cn id=811 lang=python3
#
# [811] 子域名访问计数
#

from collections import defaultdict
# @lc code=start
from typing import List

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domaincounts = defaultdict(int)
        for cpdomain in cpdomains:
            rep, domain = cpdomain.split()
            subdomain = domain.split(".")
            for i in range(len(subdomain)):
                domaincounts[".".join(subdomain[i:])] += int(rep)
        return ["{} {}".format(v, k) for k, v in domaincounts.items()]


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.subdomainVisits(["9001 discuss.leetcode.com"])
    print(ans)
    ans = solution.subdomainVisits(
        ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
    )
    print(ans)
