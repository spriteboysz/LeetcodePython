#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#
from typing import List
# @lc code=star


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(m, m + n):
            nums1[i] = nums2[m - i]

        for i in range(0, m + n):
            for j in range(i + 1, m + n):
                if nums1[i] > nums1[j]:
                    nums1[i], nums1[j] = nums1[j], nums1[i]

# @lc code=end


if __name__ == '__main__':
    s = Solution()
    s.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
