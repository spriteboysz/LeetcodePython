#! /usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-05-16 23:20:35
LastEditTime: 2022-05-16 23:25:34
Description: 
FilePath: 剑指 Offer II 042. 最近请求次数.py
'''
#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-16 23:20:35
LastEditTime: 2022-05-16 23:21:44
Description: 
FilePath: 剑指 Offer II 042. 最近请求次数.py
"""


class RecentCounter:
    def __init__(self):
        self.val = []

    def ping(self, t: int) -> int:
        self.val.append(t)
        while self.val[0] < t - 3000:
            self.val.pop(0)
        return len(self.val)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
