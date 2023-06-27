#
# @lc app=leetcode.cn id=454 lang=python3
#
# [454] 四数相加 II
#

from collections import defaultdict

from typing import List


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        countAB = defaultdict(int)
        for a in nums1:
            for b in nums2:
                countAB[a + b] += 1
        count = 0
        for c in nums3:
            for d in nums4:
                if -c - d in countAB:
                    count += countAB[-c - d]
        return count


if __name__ == "__main__":
    solution = Solution()
    ans = solution.fourSumCount(
        nums1=[1, 2], nums2=[-2, -1], nums3=[-1, 2], nums4=[0, 2]
    )
    print(ans)
    ans = solution.fourSumCount(nums1=[0], nums2=[0], nums3=[0], nums4=[0])
    print(ans)
