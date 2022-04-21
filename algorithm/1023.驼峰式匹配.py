#
# @lc app=leetcode.cn id=1023 lang=python3
#
# [1023] 驼峰式匹配
#

# @lc code=start
from typing import List


class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        match = []
        for query in queries:
            j = 0
            for i in range(len(query)):
                if query[i] == pattern[j]:
                    j += 1
                elif query[i].islower():
                    pass
                else:
                    match.append(False)
                    break
                if j == len(pattern):
                    # match.append(len(list(filter(lambda el: el.isupper(), query[i + 1 :]))) == 0)
                    match.append(not query[i + 1 :] or query[i + 1 :].islower())
                    break
            else:
                match.append(False)
        return match


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # ans = solution.camelMatch(
    #     queries=["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"],
    #     pattern="FB",
    # )
    # print(ans)
    # ans = solution.camelMatch(
    #     queries=["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"],
    #     pattern="FoBa",
    # )
    # print(ans)
    # ans = solution.camelMatch(
    #     queries=["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"],
    #     pattern="FoBaT",
    # )
    # print(ans)
    ans = solution.camelMatch(
        [
            "IXfGawluvnCa",
            "IsXfGaxwulCa",
            "IXfGawlqtCva",
            "IXjfGawlmeCa",
            "IXfGnaynwlCa",
            "IXfGcamwelCa",
        ],
        "IXfGawlCa",
    )
    print(ans)
