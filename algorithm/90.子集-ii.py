#
# @lc app=leetcode.cn id=90 lang=python3
#
# [90] 子集 II
#

# @lc code=start
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        for num in nums:
            for i in range(len(subsets)):
                for item in [subsets[i] + [num]]:
                    if sorted(item) not in subsets:
                        subsets.append(list(sorted(item)))
                #subsets.append(subsets[i] + [num])
        return subsets
# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    arguments = [[1, 2, 2], [0], [4, 4, 4, 1, 4]]
    for i, args in enumerate(arguments):
        print("=== {:02d} INPUT ===".format(i + 1))
        print(args)
        print("=== DEBUG ===")
        answer = solution.subsetsWithDup(args)
        print("=== OUTPUT ===")
        print(answer)
