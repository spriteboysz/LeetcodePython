#
# @lc app=leetcode.cn id=1255 lang=python3
#
# [1255] 得分最高的单词集合
#

# @lc code=start
from typing import List
from string import ascii_lowercase


class Solution:
    def maxScoreWords(
        self, words: List[str], letters: List[str], score: List[int]
    ) -> int:
        lettercount = [0] * 26
        for letter in letters:
            lettercount[ascii_lowercase.index(letter)] += 1
        print(lettercount)
        points = 0
        for word in words:
            wordcount = [0] * 26
            for letter in word:
                wordcount[ascii_lowercase.index(letter)] += 1
            if (
                len(
                    list(
                        filter(
                            lambda el: el < 0,
                            map(lambda l, w: l - w, lettercount, wordcount),
                        )
                    )
                )
                == 0
            ):
                points += sum(map(lambda w, s: w * s, wordcount, score))
        return points


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    ans = solution.maxScoreWords(
        words=["dog", "cat", "dad", "good"],
        letters=["a", "a", "c", "d", "d", "d", "g", "o", "o"],
        score=[
            1,
            0,
            9,
            5,
            0,
            0,
            3,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            2,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
        ],
    )
    print(ans)
