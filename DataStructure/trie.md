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