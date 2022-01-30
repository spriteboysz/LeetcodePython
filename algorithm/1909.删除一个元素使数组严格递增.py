#
# @lc app=leetcode.cn id=1909 lang=python3
#
# [1909] 删除一个元素使数组严格递增
#

# @lc code=start
from typing import List


class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        if len(nums) - len(set(nums)) > 1:
            return False
        else:
            sequence = list(sorted(nums))
            for i in range(1, len(nums)):
                if nums[i - 1] > nums[i]:
                    
                    sequence.remove(nums[i - 1])
                    nums.remove(nums[i - 1])
                    print(sequence)
                    print(nums)
                    return True if nums == sequence else False
            else:
                return True


# @lc code=end


if __name__ == "__main__":
    s = Solution()
    # print(s.canBeIncreasing([1, 2, 10, 5, 7]))
    # print(s.canBeIncreasing([2, 3, 1, 2]))
    # print(s.canBeIncreasing([1, 1, 1]))
    # print(s.canBeIncreasing([1, 2, 3]))
    print(s.canBeIncreasing([105, 924, 32, 968]))
