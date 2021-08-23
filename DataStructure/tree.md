# Binary Tree

## traversal
### pre_order
```python
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def preorder(root):
    if not root:
        return []
    return [root.val] + preorder(root.left) + preorder(root.right)
    
def preorder1(root):
    def dfs(root):
        if root:
            res.append(root.val)
            dfs(root.left)
            dfs(root.right) 
    res = []
    dfs(root)
    return res

def preorder2(root):
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

def preorder3(root):
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
    
# []
root = None
print(preorder(root))
# [1]
root = TreeNode(1)
print(preorder(root))
# [1, 2]
root = cur =  TreeNode(1)
cur.left = TreeNode(2)
print(preorder(root))

# [1, null, 2]
root = TreeNode(1)
root.right = TreeNode(2)
print(preorder(root))

# [1, null, 2, 3]
root = cur = TreeNode(1)
cur.right = TreeNode(2)
cur = cur.right
cur.left = TreeNode(3)
print(preorder(root))
```

### in_order
```python
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def inorder(root):
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)
    
def inorder1(root):
    def dfs(root):
        if root:
            dfs(root.left)
            res.append(root.val)
            dfs(root.right) 
    res = []
    dfs(root)
    return res

def inorder2(root):
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

# []
root = None
print(inorder(root))
# [1]
root = TreeNode(1)
print(inorder(root))
# [1, 2]
root = cur =  TreeNode(1)
cur.left = TreeNode(2)
print(inorder(root))

# [1, null, 2]
root = TreeNode(1)
root.right = TreeNode(2)
print(inorder(root))

# [1, null, 2, 3]
root = cur = TreeNode(1)
cur.right = TreeNode(2)
cur = cur.right
cur.left = TreeNode(3)
print(inorder(root))
```

### post_order
```python
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def postorder(root):
    if not root:
        return []
    return postorder(root.left) + postorder(root.right) + [root.val] 
    
def postorder1(root):
    def dfs(root):
        if root:
            dfs(root.left)
            dfs(root.right) 
            res.append(root.val)

    res = []
    dfs(root)
    return res

def postorder2(root):
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

def postorder3(root):
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


    

# []
root = None
print(postorder(root))
# [1]
root = TreeNode(1)
print(postorder(root))
# [1, 2]
root = cur =  TreeNode(1)
cur.left = TreeNode(2)
print(postorder(root))

# [1, null, 2]
root = TreeNode(1)
root.right = TreeNode(2)
print(postorder(root))

# [1, null, 2, 3]
root = cur = TreeNode(1)
cur.right = TreeNode(2)
cur = cur.right
cur.left = TreeNode(3)
print(postorder(root))
```

### levelOrder

### N Tree
