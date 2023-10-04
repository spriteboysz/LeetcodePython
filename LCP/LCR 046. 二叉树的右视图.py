#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-10-01 22:18
FileName: LCP
Description:LCR 046. 二叉树的右视图.py 
"""
from collections import deque
from typing import List

from common.TreeNode import TreeNode


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        right = []
        if not root:
            return right
        queue = deque([root])
        while queue:
            n, level = len(queue), 0
            for i in range(n):
                node = queue.popleft()
                level = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            right.append(level)
        return right


if __name__ == '__main__':
    print(Solution().rightSideView(TreeNode.create("[1,2,3,null,5,null,4]")))
