#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        while "()" in s or "[]" in s or "{}" in s:
            for item in ["()", "[]", "{}"]:
                num = s.count(item)
                s = s.replace(item, "", num)

        return len(s) == 0
# @lc code=end


if __name__ == '__main__':
    s = Solution()
    print(s.isValid("([])"))
    # print(s.isValid("{[[]])"))
    
