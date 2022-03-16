#
# @lc app=leetcode.cn id=2115 lang=python3
#
# [2115] 从给定原材料中找到所有可以做出的菜
#

# @lc code=start
from typing import List


class Solution:
    def findAllRecipes(
        self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]
    ) -> List[str]:
        pass


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.findAllRecipes(
        recipes=["bread"],
        ingredients=[["yeast", "flour"]],
        supplies=["yeast", "flour", "corn"],
    )
    print(ans)
