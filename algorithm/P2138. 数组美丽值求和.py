#
# @lc app=leetcode.cn id=2260 lang=python3
#
# [2138] 将字符串拆分为若干长度为 k 的组
#
from typing import List


class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        if len(s) % k != 0:
            s += fill * (k - len(s) % k)
        divide = []
        for i in range(0, len(s) - k + 1, k):
            divide.append(s[i:i + k])
        return divide


if __name__ == '__main__':
    solution = Solution()
    print(solution.divideString(s="abcdefghi", k=3, fill="x"))
