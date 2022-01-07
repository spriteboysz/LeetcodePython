#
# @lc app=leetcode.cn id=219 lang=python3
#
# [219] 存在重复元素 II
#
#no submit!
# @lc code=start
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for i in range(0, len(nums)-1):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j] and j - i <= k:
                    return True
        return False
# @lc code=end


if __name__ == '__main__':
    s = Solution()
    print(s.containsNearbyDuplicate([1, 2, 3, 1], 2))
