#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-04-20 11:41
FileName: algorithm
Description:P3114. 替换字符可以得到的最晚时间.py 
"""


class Solution:
    def findLatestTime(self, s: str) -> str:
        for minute in range(12 * 60 - 1, -1, -1):
            hh, mm = divmod(minute, 60)
            cur = '{:02}:{:02}'.format(hh, mm)
            for i in range(5):
                if s[i] != '?' and s[i] != cur[i]:
                    break
            else:
                return cur
        return '00:00'


if __name__ == '__main__':
    print(Solution().findLatestTime(s="1?:?4"))
