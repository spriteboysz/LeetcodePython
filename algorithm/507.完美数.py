#
# @lc app=leetcode.cn id=507 lang=python3
#
# [507] 完美数
#

# @lc code=start
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        lst = []
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                lst.append(i + num / i)

        if num == 1:
            return False
        else:        
            return num == 1 + sum(lst)
# @lc code=end

if __name__ == '__main__':
    s = Solution()
    print(s.checkPerfectNumber(6))
    
