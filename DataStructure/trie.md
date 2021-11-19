```python
class Trie:
    def __init__(self) -> None:
        self.root = {}
    
    def insert(self, word):
        cur = self.root
        for c in word:
            if c not in cur:
                cur[c] = {}
            cur = cur[c]
        cur['#'] = True

    def search(self, word):
        cur = self.root
        for c in word:
            if c not in cur:
                return False
            cur = cur[c]
        # return cur['#']
        return True if cur and '#' in cur else False

    def startWith(self, prefix):
        cur = self.root
        for c in prefix:
            if c not in cur:
                return False
            cur = cur[c]
        return True   
```

```python
from collections import defaultdict
class TrieNode:
    def __init__(self) -> None:
        self.children = defaultdict(TrieNode)
        self.isWord = False

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for c in word:
            node = node.children[c]
        node.isWord = True

    def search(self, word):
        node = self.root
        for c in word:
            node = node.children.get(c)
            if not node:
                return False
        return node.isWord

    def startWith(self, prefix):
        node = self.root
        for c in prefix:
            node = node.children.get(c)
            if not node:
                return False
        return True        
```

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True

    def search(self, word):
        cur =self.root
        for c in word:
            if c not in cur.children:
                return False
            cur =cur.children[c]
        return cur.isWord

    def startWith(self, prefix):
        cur =self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True       
```

