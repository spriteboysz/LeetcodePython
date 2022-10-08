#
# @lc app=leetcode.cn id=1578 lang=python3
#
# [1578] 使绳子变成彩色的最短时间
#

# @lc code=start
from typing import List


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        count, i, j = 0, 1, 0
        while i < len(colors) and j < len(neededTime):
            if colors[i] == colors[i - 1]:
                if neededTime[j] <= neededTime[i]:
                    count += neededTime[j]
                    j = i
                else:
                    count += neededTime[i]
            else:
                j = i
            i += 1
        return count


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.minCost(colors="abaac", neededTime=[1, 2, 3, 4, 5])
    print(ans)
