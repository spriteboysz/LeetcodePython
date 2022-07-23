#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-02-11 23:32:38
LastEditTime: 2022-02-11 23:39:41
Description: 
FilePath: 1817.查找用户活跃分钟数.py
'''
#
# @lc app=leetcode.cn id=1817 lang=python3
#
# [1817] 查找用户活跃分钟数
#

from collections import defaultdict
# @lc code=start
from typing import List

class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        users = defaultdict(set)
        for log in logs:
            users[log[0]].add(log[1])

        answer = [0] * k
        for v in users.values():
            answer[len(v) - 1] += 1
        return answer
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.findingUsersActiveMinutes(
        logs=[[0, 5], [1, 2], [0, 2], [0, 5], [1, 3]], k=5))
    print(s.findingUsersActiveMinutes(logs=[[1, 1], [2, 2], [2, 3]], k=4))
