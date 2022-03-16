#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-16 19:26:16
LastEditTime: 2022-03-16 19:34:03
Description: 
FilePath: 985.查询后的偶数和.py
"""
#
# @lc app=leetcode.cn id=985 lang=python3
#
# [985] 查询后的偶数和
#

# @lc code=start
from typing import List


class Solution:
    def sumEvenAfterQueries(
        self, nums: List[int], queries: List[List[int]]
    ) -> List[int]:
        cur = sum(filter(lambda el: el % 2 == 0, nums))
        sumeven = []
        for value, index in queries:
            if nums[index] % 2 == 0:
                if value % 2 == 0:
                    cur += value
                else:
                    cur -= nums[index]
            else:
                if value % 2 == 0:
                    pass
                else:
                    cur += value + nums[index]
            nums[index] += value
            sumeven.append(cur)

        return sumeven


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.sumEvenAfterQueries(
        nums=[1, 2, 3, 4], queries=[[1, 0], [-3, 1], [-4, 0], [2, 3]]
    )
    print(ans)
