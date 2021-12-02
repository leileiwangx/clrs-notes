# Binary Tree

## traversal
### pre_order
```python
def preorder(root):
    if not root: return []
    res = []
    stack = [root]
    while stack:
        node = stack.pop()
        res.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return res

def preorder(root):
    res = []
    cur = root
    stack = []
    while stack or cur:
        while cur:
            res.append(cur.val)
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        cur = cur.right
    return res
```

### in_order
```python
def inorder(root):
    if not root: return []
    res = []
    node = root
    stack = []
    while stack or node:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        res.append(node.val)
        node = node.right
    return res
```

### post_order
```python
def postorder(root):
    if not root: return []
    stack = [root]
    res = []
    while stack :
        cur = stack.pop()
        res.append(cur.val)
        if cur.left:
            stack.append(cur.left)
        if cur.right:
            stack.append(cur.right)
    return res[::-1]

def postorder(root):
    if not root: return []
    cur = root
    pre = None
    stack = []
    res = []
    while stack or cur:
        while cur:
            stack.append(cur)
            cur = cur.left
        # cur = stack.pop()
        cur = stack[-1]
        if cur.right and cur.right != pre:
            cur = cur.right
        else:
            stack.pop()
            res.append(cur.val)
            pre = cur
            cur = None ##
    return res
```

### levelOrder
```python
def levelOrder(root: TreeNode):
    if not root:
        return []
    cur = [root]
    res = []
    while cur:
        res.append([node.val for node in cur])
        temp = []
        for node in cur:
            if node.left:
                temp.append(node.left)
            if node.right:
                temp.append(node.right)
        cur = temp
    return res
```
### N Tree
