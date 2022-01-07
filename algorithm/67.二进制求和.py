#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        print(int(a))
        c = int(bin(a)) + int(bin(b))
        return bin(c)
# @lc code=end

if __name__ == '__main__':
    s = Solution()
    print(s.addBinary("11", "1"))

