#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-02-06 22:40:21
LastEditTime: 2022-02-06 23:13:15
Description: 
FilePath: 1560.圆形赛道上经过次数最多的扇区.py
'''
#
# @lc app=leetcode.cn id=1560 lang=python3
#
# [1560] 圆形赛道上经过次数最多的扇区
#

# @lc code=start
from typing import List


class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        visited = [0] * n
        for i in range(1, len(rounds)):
            start, end = rounds[i - 1] - 1, rounds[i] - 1
            if start <= end:
                for j in range(start, end + 1):
                    visited[j] += 1
            else:
                for j in range(start, n):
                    visited[j] += 1
                for j in range(0, end + 1):
                    visited[j] += 1
            if i - 1 != 0:
                visited[start] -= 1
        maximum = max(visited)
        indies = []
        for i in range(len(visited)):
            if visited[i] == maximum:
                indies.append(i + 1)
        return indies

# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.mostVisited(4, [1, 3, 1, 2]))
    print(s.mostVisited(2, [2, 1, 2, 1, 2, 1, 2, 1, 2]))
    print(s.mostVisited(7, [1, 3, 5, 7]))
