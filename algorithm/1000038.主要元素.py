#
# @lc app=leetcode.cn id=1000038 lang=python3
#
# [面试题 17.10] 主要元素
#

# @lc code=start
from typing import List
from collections import defaultdict


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
            if count[num] > n // 2:
                return num
        else:
            return -1


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    ans = solution.majorityElement([1, 2, 5, 9, 5, 9, 5, 5, 5])
    print(ans)
    ans2 = solution.majorityElement([3, 2])
    print(ans2)
    ans3 = solution.majorityElement([2, 2, 1, 1, 1, 2, 2])
    print(ans3)
