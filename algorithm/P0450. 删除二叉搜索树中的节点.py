#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-05-03 16:35
FileName: algorithm
Description:P0450. 删除二叉搜索树中的节点.py 
"""
from typing import Optional

from common.TreeNode import TreeNode


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            values.append(root.val)
            dfs(root.right)

        def create(left, right):
            if left >= right:
                return None
            mid = left + (right - left) // 2
            root = TreeNode(values[mid])
            root.left = create(left, mid)
            root.right = create(mid + 1, right)
            return root

        values = []
        dfs(root)
        if key not in values:
            return root
        values.remove(key)
        return create(0, len(values))


if __name__ == '__main__':
    root = TreeNode.create('[5,3,6,2,4,null,7]')
    print(Solution().deleteNode(root, 5))
