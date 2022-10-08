#
# @lc app=leetcode.cn id=1108 lang=python3
#
# [1108] IP 地址无效化
#

# @lc code=start
class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")
# @lc code=end


if __name__ == '__main__':
    s = Solution()
    s.defangIPaddr("1.1.1.1")
