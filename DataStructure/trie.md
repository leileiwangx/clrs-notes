### defaultdict
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

trie = Trie()
print(trie.insert('hello'))
print(trie.insert('hel'))
print(trie.search('hello'))
print(trie.search('hell'))
print(trie.startWith('hel'))
print(trie.startWith('helo'))
```

### dict
```python
class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.isWord = False

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()
    
    def insert(self, word):
        cur = self.root
        for c in word:
            if c in cur.children:
                cur = cur.children[c]
            else:
                node = TrieNode()
                cur.children[c] = node
                cur = node
        cur.isWord = True

    def search(self, word):
        cur = self.root
        for c in word:
            cur = cur.children.get(c, None)
            if not cur:
                return False
        return cur.isWord

    def startWith(self, prefix):
        cur = self.root
        for c in prefix:
            cur = cur.children.get(c, None)
            if not cur:
                return False
        return True        
```

### dict2
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