#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-12 23:15
LastEditTime: 2022-06-12 23:15
Description:
FilePath: 1861.旋转盒子.py
"""

from typing import List


class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        n, m = len(box), len(box[0])
        for i in range(n):
            new = "".join(box[i]).split("*")
            # print(new)
            for j in range(len(new)):
                new[j] = "".join(sorted(new[j], key=lambda el: el == "#"))
            box[i] = list("*".join(new))

        box.reverse()
        return list(map(list, zip(*box)))


if __name__ == '__main__':
    solution = Solution()
    ans = solution.rotateTheBox(box=[["#", ".", "#"]])
    print(ans)
    ans = solution.rotateTheBox(box=[["#", ".", "*", "."],
                                     ["#", "#", "*", "."]])
    print(ans)
    ans = solution.rotateTheBox(box=[["#", "#", "*", ".", "*", "."],
                                     ["#", "#", "#", "*", ".", "."],
                                     ["#", "#", "#", ".", "#", "."]])
    print(ans)
