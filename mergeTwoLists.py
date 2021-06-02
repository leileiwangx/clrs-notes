# Merge two sorted linked lists and return it as a sorted list.
# The list should be made by splicing together the nodes of the first two lists.

class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None

# convert array to linked list
def convertArrayToLinkedList(arr):
    head = ListNode(arr[0])
    cur = head
    for i in range(1, len(arr)):
        cur.next = ListNode(arr[i])
        cur = cur.next
    return head

# return array format of linked list
def convertLinkedListToArray(head):
    res = []
    cur = head
    while cur:
        res.append(cur.val)
        cur = cur.next
    return res

class Solution():
    def mergeTwoLists(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val > l2.val:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
        else:
            l1.next = self.mergeTwoLists(l1.next,l2)
            return l1

def main():
    head1 = convertArrayToLinkedList([1, 2, 4])
    head2 = convertArrayToLinkedList([1, 3, 4])
    solution = Solution()
    mergedLinkedList = solution.mergeTwoLists(head1, head2)
    print(convertLinkedListToArray(mergedLinkedList))
    # output [1, 1, 2, 3, 4, 4]

if __name__ == "__main__":
    main()