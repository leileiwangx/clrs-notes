```python
def findFather(i):
    if fathers[i] != i:
        fathers[i] = findFather(fathers[i])
    return fathers[i]

def union(i, j):
    father_i = findFather(i)
    father_j = findFather(j)
    if father_i != father_j:
        fathers[father_i] = father_j
        return True
    return False
    
fathers = [i for i in range(n)]
```