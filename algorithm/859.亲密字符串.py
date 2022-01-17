#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-17 23:40:39
LastEditTime: 2022-01-17 23:51:56
Description: 
FilePath: 859.亲密字符串.py
'''
#
# @lc app=leetcode.cn id=859 lang=python3
#
# [859] 亲密字符串
#

# @lc code=start


class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        else:
            count = 0
            s1, g1 = [], []
            for i, j in zip(list(s), list(goal)):
                if i != j:
                    count += 1
                    s1.append(i)
                    g1.append(j)
            if count == 2 and s1 == g1[::-1]:
                return True
            elif count == 0 and max(map(lambda el: s.count(el), set(list(s)))) >= 2:
                return True
            else:
                return False

# @lc code=end


if __name__ == '__main__':
    s = Solution()
    print(s.buddyStrings("ab", "ab"))
