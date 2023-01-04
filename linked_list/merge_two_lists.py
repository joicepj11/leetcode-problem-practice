"""

21. Merge Two Sorted Lists


You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list

Example 1:

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]

"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        temp = head

        while list1 is not None and list2 is not None:
            if list1.val > list2.val:
                temp2 = list2
                list2 = list2.next
                temp2.next = None
                temp.next = temp2
            else:
                temp2 = list1
                list1 = list1.next
                temp2.next = None
                temp.next = temp2
            temp = temp.next

        if list2 is not None:
            temp.next = list2

        if list1 is not None:
            temp.next = list1

        return head.next

if __name__ == '__main__':
    s = Solution()
    t = ListNode(0)
    temp = t

    for i in range(1, 10):
        temp.next = ListNode(i)
        temp = temp.next

    t2 = ListNode(0)
    temp = t2
    for i in range(1, 10):
        temp.next = ListNode(i)
        temp = temp.next

    a = s.mergeTwoLists( t, t2)

    while a is not None:
        print(a.val, sep=" ",end=" ")
        a = a.next
