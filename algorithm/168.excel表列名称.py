#
# @lc app=leetcode.cn id=168 lang=python3
#
# [168] Excel表列名称
#
# 未完成
# @lc code=start
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        s = ""
        if columnNumber < 27:
            s = chr(ord('a')+columnNumber-1)
        else:
            shang = inputStr // 26
            yushuList.append(inputStr % 26)
            while shang > 26:
                yushu = shang % 26
                yushuList.append(yushu)
                shang = shang // 26
            yushuList.append(shang)
        for x in range(len(yushuList)-1, -1, -1):
            restStr = restStr + chr(yushuList[x]+ord('a')-1)

        return restStr


# @lc code=end

if __name__ == '__main__':
    s = Solution()
    print(s.convertToTitle(27))
