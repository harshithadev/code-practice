
# Reverse a Singly Linked List
# Write a function to reverse a singly linked list. The function should return a new linked list that is the reverse of the original list.

# Example:

# Original singly linked list:   1 -> 2 -> 3 -> 4 -> 5

# Reversed singly linked list:  5 -> 4 -> 3 -> 2 -> 1

def reverse(self):
    prev_node = None
    current_node = self.head
    while current_node is not None:
        next_node = current_node.next
        current_node.next = prev_node
        prev_node = current_node
        current_node = next_node
    self.head, self.tail = self.tail, self.head
