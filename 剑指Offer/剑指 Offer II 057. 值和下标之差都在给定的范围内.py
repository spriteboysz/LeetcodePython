#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-18 23:40:52
LastEditTime: 2022-05-18 23:40:52
Description: 
FilePath: 剑指 Offer II 057. 值和下标之差都在给定的范围内.py
"""

from typing import List
from sortedcontainers import SortedList
from bisect import bisect_left


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        st = SortedList()
        for i, num in enumerate(nums):
            st.add(num)
            index = bisect_left(st, num)
            if index < len(st) - 1 and st[index + 1] - st[index] <= t:
                return True
            if index > 0 and st[index] - st[index - 1] <= t:
                return True
            if len(st) > k:
                st.remove(nums[i - k])
        return False


if __name__ == "__main__":
    solution = Solution()
    ans = solution.containsNearbyAlmostDuplicate(nums=[1, 5, 9, 1, 5, 9], k=2, t=3)
    print(ans)
    ans = solution.containsNearbyAlmostDuplicate(nums=[1, 2, 3, 1], k=3, t=0)
    print(ans)
    ans = solution.containsNearbyAlmostDuplicate([7, 1, 3], 2, 3)
    print(ans)
