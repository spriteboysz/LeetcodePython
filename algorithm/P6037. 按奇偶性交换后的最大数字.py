#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-12 23:31:11
LastEditTime: 2022-04-12 23:33:04
Description: 
FilePath: 6037.按奇偶性交换后的最大数字.py
"""
#
# @lc app=leetcode.cn id=6037 lang=python3
#
# [6037] 按奇偶性交换后的最大数字
#

# @lc code=start
class Solution:
    def largestInteger(self, num: int) -> int:
        even, evenindex, odd, oddindex = [], [], [], []
        for i, item in enumerate(str(num)):
            if int(item) % 2 == 0:
                even.append(item)
                evenindex.append(i)
            else:
                odd.append(item)
                oddindex.append(i)
        even.sort()
        odd.sort()
        largest = ""
        for i in range(len(str(num))):
            if i in evenindex:
                largest += even.pop()
            else:
                largest += odd.pop()
        return int(largest)


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    ans = solution.largestInteger(1234)
    print(ans)
    ans = solution.largestInteger(65875)
    print(ans)
    ans = solution.largestInteger(247)
    print(ans)
