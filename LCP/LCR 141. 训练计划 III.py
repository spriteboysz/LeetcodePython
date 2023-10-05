#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-10-03 22:21
FileName: LCP
Description:LCR 141. 训练计划 III.py 
"""
from typing import Optional

from common.ListNode import ListNode


class Solution:
    def trainningPlan(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def recur(cur, pref):
            if not cur:
                return pref
            res = recur(cur.next, cur)
            cur.next = pref
            return res

        return recur(head, None)


if __name__ == '__main__':
    print(Solution().trainningPlan(ListNode.create("[1,2,3,4,5]")))
