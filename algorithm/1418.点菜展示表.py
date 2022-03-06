#
# @lc app=leetcode.cn id=1418 lang=python3
#
# [1418] 点菜展示表
#

# @lc code=start
from typing import List
from collections import defaultdict


class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        abc = defaultdict(list(defaultdict(int)))
        print(abc)


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.displayTable(
        [
            ["David", "3", "Ceviche"],
            ["Corina", "10", "Beef Burrito"],
            ["David", "3", "Fried Chicken"],
            ["Carla", "5", "Water"],
            ["Carla", "5", "Ceviche"],
            ["Rous", "3", "Ceviche"],
        ]
    )
    print(ans)
