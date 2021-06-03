'''
preorder = [3,9,20,15,7], inorder = [9,3,15,20,7] Output: [3,9,20,null,null,15,7]
Input: preorder = [-1], inorder = [-1] Output: [-1]
'''

import collections
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

# def converListToTree(vals):
#     if len(vals) == 0:
#         return None
#     que = collections.deque()
#     fill_left = True
#     for val in vals:
#         node = TreeNode(val) if val else None
#         if len(que) == 0:
#             root = node
#             que.append(node)
#         elif fill_left:
#             que[0].left = node
#             fill_left = False
#             if node:
#                 que.append(node)
#         else:
#             que[0].right = node
#             if node:
#                 que.append(node)
#             que.popleft()
#             fill_left = True
#     return root

def converListToTree(arr, index):
    pNode = None
    if index < len(arr):
        if not arr[index]:
            return
        pNode = TreeNode(arr[index])
        pNode.left = converListToTree(arr, 2 * index + 1)
        pNode.right = converListToTree(arr, 2* index + 2)
    return pNode

def converTreeToList(root):
    if not root:
        return []
    stack = [root]
    res = []
    while stack:
        res += [node.val if node else None for node in stack]
        temp = []
        for node in stack:
            if node:
                temp.append(node.left if node.left else None)
                temp.append(node.right if node.right else None)
        stack = temp

    # remove end None
    i = len(res) - 1
    while i >= 0:
        if res[i] != None:
            break
        i -= 1
    return res[: i + 1]

class Solution:
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder: return None
        root = TreeNode(preorder[0])
        idx = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1 : idx + 1], inorder[ : idx])
        root.right = self.buildTree(preorder[idx + 1 :], inorder[idx + 1 :])
        return root

def main():
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]
    solution = Solution()
    root = solution.buildTree(preorder, inorder)
    print(converTreeToList(root))
    # output : [3, 9, 20, None, None, 15, 7]


if __name__ == '__main__':
    main()
