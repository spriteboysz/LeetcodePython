#
# @lc app=leetcode.cn id=728 lang=python3
#
# [728] 自除数
#
from typing import List


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        lst = []
        for i in range(left, right + 1):
            for item in str(i):
                if int(item) == 0 or i % int(item) != 0:
                    break
            else:
                lst.append(i)
        return lst


if __name__ == '__main__':
    s = Solution()
    print(s.selfDividingNumbers(1, 22))
