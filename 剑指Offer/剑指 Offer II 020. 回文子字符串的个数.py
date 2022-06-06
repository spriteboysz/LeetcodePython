#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-06 23:11
LastEditTime: 2022-06-06 23:11
Description:
FilePath: 剑指 Offer II 020. 回文子字符串的个数.py
"""


class Solution:
    def countSubstrings(self, s: str) -> int:
        substrings = []
        for i in range(len(s)):
            cur = ""
            for j in range(i, len(s)):
                cur += s[j]
                substrings.append(cur)

        return len(list(filter(lambda el: el == el[::-1], substrings)))
        # count = 0
        # for string in substrings:
        #     if string == string[::-1]:
        #         count += 1
        # return count


if __name__ == '__main__':
    solution = Solution()
    ans = solution.countSubstrings("abc")
    print(ans)
