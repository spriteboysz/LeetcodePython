#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-20 20:24:20
LastEditTime: 2022-02-20 20:29:57
Description: 
FilePath: 2075.解码斜向换位密码.py
"""


#
# @lc app=leetcode.cn id=2075 lang=python3
#
# [2075] 解码斜向换位密码
#

# @lc code=start


class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        if encodedText == "":
            return ""
        n = len(encodedText) // rows
        encoded = []
        for i in range(0, len(encodedText), n):
            cur = encodedText[i: i + n]
            cur = cur[(i // n):] + cur[: (i // n)]
            encoded.append(cur)
        decode = []
        for item in zip(*encoded):
            decode += list(item)
        return "".join(decode).rstrip()


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans1 = solution.decodeCiphertext("ch   ie   pr", 3)
    print(ans1)
    ans2 = solution.decodeCiphertext("iveo    eed   l te   olc", 4)
    print(ans2)
    ans3 = solution.decodeCiphertext("coding", 1)
    print(ans3)
    ans4 = solution.decodeCiphertext(" b  ac", 2)
    print(ans4)
