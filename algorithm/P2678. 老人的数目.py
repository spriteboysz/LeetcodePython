#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-06-24 23:04
FileName: algorithm/P2678. 老人的数目.py
Description: 
"""
from typing import List


class Solution:
    def countSeniors(self, details: List[str]) -> int:
        return len(list(filter(lambda el: int(el[11:13]) > 60, details)))


if __name__ == '__main__':
    print(Solution().countSeniors(details=["7868190130M7522", "5303914400F9211", "9273338290F4010"]))
