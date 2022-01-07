#
# @lc app=leetcode.cn id=557 lang=python3
#
# [557] 反转字符串中的单词 III
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        lst1 = s.split()
        lst2 = []
        for item in lst1:
            lst2.append(item[::-1])

        print(" ".join())
# @lc code=end

