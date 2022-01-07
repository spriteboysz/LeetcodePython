#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除有序数组中的重复项
#

# @lc code=start

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            for j in range(len(nums) - 1, i, -1):
                if nums[j] == nums[i]:
                    del nums[j]

        return len(nums)
# @lc code=end

if __name__ == '__main__':
    s = Solution()
    ret = s.removeDuplicates([1,1,2])
    print(ret)
    
