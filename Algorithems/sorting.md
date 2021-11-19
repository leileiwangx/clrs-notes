## heap sort
```python
def heap_sort(nums):
    def heapify(n, i):
        left = 2 * i + 1
        right = 2 * i + 2
        largest = i
        if left < n and nums[left] > nums[i]:
            largest = left
        if right < n and nums[right] > nums[largest]:
            largest = right
        if largest != i:
            nums[i], nums[largest] = nums[largest], nums[i]
        # heapify(n, largest)
            heapify(n, largest)

    # o(1) space
    def heapify2(n, i):
        while True:
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2
            if left < n and nums[i] < nums[left]:
                largest = left
            if right < n and nums[largest] < nums[right]:
                largest = right
            if largest == i:
                break
            nums[largest], nums[i] = nums[i], nums[largest]
            i = largest

    n = len(nums)
     # build max heap (n)
    for i in range(n // 2 - 1, -1, -1):
        heapify2(n, i)
    # heap sort (nlogn)
    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(i, 0)
    return nums
```
## quick sort
```python
import random
def quick_sort(nums):
    def partition(lo, hi):
        idx = random.randint(lo, hi)
        nums[idx], nums[hi] = nums[hi], nums[idx]
        i = lo
        pivot = nums[hi]
        for j in range(lo, hi):
            if nums[j] < pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        nums[hi], nums[i] = nums[i], nums[hi]
        return i

    def quickSort(lo, hi):
        if lo >= hi: return
        mi = partition(lo, hi)
        quickSort(lo, mi - 1)
        quickSort(mi + 1, hi)

    quickSort(0, len(nums) - 1)
    return nums
```
## merge sort
### space logn
```python
def merge_sort(nums):
    def merge(lo, mi, hi):
        k = i = lo
        j = mi + 1 # j = mi
        while i <= mi and j <= hi:
            if nums[i] < nums[j]:
                temp[k] = nums[i]
                k += 1
                i += 1
            else:
                temp[k] = nums[j]
                j += 1
                k += 1
        while i <= mi:
            temp[k] = nums[i]
            i += 1
            k += 1
        while j <= hi:
            temp[k] = nums[j]
            j += 1
            k += 1
        nums[lo : hi + 1] = temp[lo : hi + 1]
    # space logn
    def sort(lo, hi):
        if lo >= hi:
            return
        mi = lo + ((hi - lo) >> 1)
        sort(lo, mi)
        # sort(mi, hi)
        sort(mi + 1, hi)
        merge(lo, mi, hi)

    temp = nums[:]
    sort(0, len(nums) - 1)
    return nums
```
### space o(1) merge sort

## count sort