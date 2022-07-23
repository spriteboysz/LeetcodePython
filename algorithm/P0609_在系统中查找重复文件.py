#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-26 22:58:16
LastEditTime: 2022-02-26 23:09:56
Description: 
FilePath: 609.在系统中查找重复文件.py
"""
#
# @lc app=leetcode.cn id=609 lang=python3
#
# [609] 在系统中查找重复文件
#

from collections import defaultdict
# @lc code=start
from typing import List

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        contents = defaultdict(list)
        for path in paths:
            directory, *files = path.split()
            for file in files:
                name, content = file.replace(")", "").split("(")
                contents[content].append(directory + "/" + name)
        return [v for v in contents.values() if len(v) >= 2]


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.findDuplicate(
        [
            "root/a 1.txt(abcd) 2.txt(efgh)",
            "root/c 3.txt(abcd)",
            "root/c/d 4.txt(efgh)",
            "root 4.txt(efgh)",
        ]
    )
    print(ans)
    ans = solution.findDuplicate(
        paths=[
            "root/a 1.txt(abcd) 2.txt(efgh)",
            "root/c 3.txt(abcd)",
            "root/c/d 4.txt(efgh)",
        ]
    )
    print(ans)
    ans = solution.findDuplicate(
        [
            "root/a 1.txt(abcd) 2.txt(efsfgh)",
            "root/c 3.txt(abdfcd)",
            "root/c/d 4.txt(efggdfh)",
        ]
    )
    print(ans)
