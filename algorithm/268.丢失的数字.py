#
# @lc app=leetcode.cn id=268 lang=python3
#
# [268] 丢失的数字
#

# @lc code=start
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nn = [0] * (len(nums) + 1)
        for index in range(len(nums)):
            nn[nums[index]] = 1

        return nn.index(0)
# @lc code=end


if __name__ == '__main__':
    s = Solution()
    print(s.missingNumber([3, 0, 1]))
