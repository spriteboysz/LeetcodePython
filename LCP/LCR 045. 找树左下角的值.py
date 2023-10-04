#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-10-01 22:29
FileName: LCP
Description:LCR 045. 找树左下角的值.py 
"""
from collections import deque

from common.TreeNode import TreeNode


class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        bottom_left = root.val
        queue = deque([root])
        while queue:
            n = len(queue)
            for i in range(n):
                node = queue.popleft()
                if i == 0:
                    bottom_left = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return bottom_left


if __name__ == '__main__':
    print(Solution().findBottomLeftValue(TreeNode.create("[1,2,3,4,null,5,6,null,null,7]")))
