from typing import List
from heapq import heappop, heappush


class Solution:
    def smallestK(self, arr: List[int], k: int) -> List[int]:
        temp = []
        for num in arr:
            heappush(temp, -num)
            if len(temp) > k:
                heappop(temp)
        return [-num for num in temp]


if __name__ == '__main__':
    solution = Solution()
    ans = solution.smallestK(arr=[1, 3, 5, 7, 2, 4, 6, 8], k=4)
    print(ans)
