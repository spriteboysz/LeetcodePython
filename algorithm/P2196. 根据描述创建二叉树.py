#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-05-15 22:35
FileName: algorithm
Description:P2196. 根据描述创建二叉树.py 
"""
from collections import defaultdict
from typing import List, Optional

from common.TreeNode import TreeNode


class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = defaultdict(lambda: [-1] * 2)
        for root, val, flag in descriptions:
            if flag == 1:
                nodes[root][0] = val
            if flag == 0:
                nodes[root][1] = val
        root_val = list(set(nodes.keys()) - set(sum(list(nodes.values()), [])))[0]

        def create(node):
            if node == -1:
                return
            return TreeNode(node, create(nodes[node][0]), create(nodes[node][1]))

        return create(root_val)


if __name__ == '__main__':
    print(Solution().createBinaryTree(descriptions=[[20, 15, 1], [20, 17, 0], [50, 20, 1], [50, 80, 0], [80, 19, 1]]))
