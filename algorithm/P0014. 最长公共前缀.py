#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lens = map(len, strs)
        for i in range(min(lens), 0, -1):
            pre = []
            for item in strs:
                pre.append(item[:i])
            if len(set(pre)) == 1:
                return pre[0]
        return ""
# @lc code=end


if __name__ == '__main__':
    s = Solution()
    rst = s.longestCommonPrefix(["a"])
    print(rst)
