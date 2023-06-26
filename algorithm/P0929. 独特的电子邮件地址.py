#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-19 22:53:46
LastEditTime: 2022-01-19 23:02:28
Description:
FilePath: 929.独特的电子邮件地址.py
"""
#
# @lc app=leetcode.cn id=929 lang=python3
#
# [929] 独特的电子邮件地址
#

# @lc code=start
from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = []
        for item in emails:
            local, domain = item.split("@")
            local = local.replace(".", "")
            if "+" in local:
                local = local[:local.index("+")]
            email = local + "@" + domain
            unique.append(email)
        return len(set(unique))
# @lc code=end
