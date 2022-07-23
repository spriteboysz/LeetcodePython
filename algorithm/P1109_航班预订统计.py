#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-17 22:25:03
LastEditTime: 2022-04-17 22:28:48
Description: 
FilePath: 1109.航班预订统计.py
"""
#
# @lc app=leetcode.cn id=1109 lang=python3
#
# [1109] 航班预订统计
#

# @lc code=start
from typing import List


class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        count = [0] * n
        for first, last, seats in bookings:
            count[first - 1] += seats
            if last < n:
                count[last] -= seats
        print(count)
        for i in range(1, n):
            count[i] += count[i - 1]
        return count


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.corpFlightBookings(
        bookings=[[1, 2, 10], [2, 3, 20], [2, 5, 25]], n=5
    )
    print(ans)
