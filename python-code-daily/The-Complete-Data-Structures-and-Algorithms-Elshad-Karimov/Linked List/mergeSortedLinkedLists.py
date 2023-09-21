# # Definition for singly-linked list.
# Merge Two Sorted Linked List
# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

# Example 1:

# Input: list1 = [1,2,4], list2 = [1,3,4]

# Output: [1,1,2,3,4,4]

# Example 2:

# Input: list1 = [], list2 = []

# Output: []

# Example 3:

# Input: list1 = [], list2 = [0]

# Output: [0]


# Constraints:

# The number of nodes in both lists is in the range [0, 50].

# -100 <= Node.val <= 100

# Both list1 and list2 are sorted in non-decreasing order.


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prehead = ListNode(-1)

        prev = prehead
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next

        # At least one of l1 and l2 can still have nodes at this point, so connect
        # the non-null list to the end of the merged list.
        prev.next = l1 if l1 is not None else l2

        return prehead.next
