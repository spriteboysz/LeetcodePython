#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-14 20:24:33
LastEditTime: 2022-03-14 20:36:25
Description: 
FilePath: 841.钥匙和房间.py
"""
#
# @lc app=leetcode.cn id=841 lang=python3
#
# [841] 钥匙和房间
#

# @lc code=start
from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        unlock, keys = [0], rooms[0]
        while keys:
            for key in keys:
                unlock.append(key)
                keys.extend(rooms[key])
                keys = list(set(keys) - set(unlock))
            if len(set(unlock)) == len(rooms):
                return True
        return False


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.canVisitAllRooms(rooms=[[1], [2], [3], []])
    print(ans)
    ans = solution.canVisitAllRooms(rooms=[[1, 3], [3, 0, 1], [2], [0]])
    print(ans)
    ans = solution.canVisitAllRooms(rooms=[[1], [1]])
    print(ans)
