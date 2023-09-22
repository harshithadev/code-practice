class Node:
    """This would create a node object"""

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    """This would create an empty linked list object"""

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    # # initializer to start with one node
    # def __init__(self, value):
    #     new_node = Node(value)
    #     self.head = new_node
    #     self.tail = new_node
    #     self.length = 1

    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += "--> "
            temp_node = temp_node.next
        return result

    def append(self, value):
        """Add element to the end of the list."""
        new_node = Node(value)

        # in case of empty LL
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # in case an element(s) already exsist
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def prepend(self, value):
        """Add element to the beginning of the list."""
        new_node = Node(value)

        # in case of empty LL
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # in case an element(s) already exsist
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def insert(self, value, index):
        """Add an element at index n of the linked list"""
        if index > self.length or index < 0:
            print("Cannot add, index beyond length")
            return None
        if index == 0:
            self.prepend(value)
        elif index == self.length:
            self.append(value)
        else:
            new_node = Node(value)

            temp_node = self.head
            # i = 0
            # while i< n - 1:
            #     temp_node = temp_node.next
            #     i += 1
            for _ in range(index-1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node

        self.length += 1

    def traverse(self):
        """Traverses through the linked list and prints it."""
        current = self.head
        while current is not None:
            print(current.value, end="")
            if current.next is not None:
                print(" > ", end="")
            current = current.next
        print()

    def search(self, value):
        """Searches for a value in the list."""
        current = self.head
        # found = False
        while current is not None:
            if (current.value == value):
                # print(f"Element {value} found")
                # found = True
                return True
            current = current.next
        # if not found:
        #     print(f"Element {value} not found")
        return False

    def get(self, index):
        """Returns the value of the node in the index given."""
        if index >= self.length - 1 or index < 0:
            return False
        current = self.head
        for _ in range(index):
            current = current.next
        return current

    def set(self, index, value):
        """Updates the value of the node in the index given."""
        # if index >= self.length - 1 or index < 0:
        #     return -1
        # current = self.head
        # for _ in range(index):
        #     current = current.next
        # current.value = value
        # return value
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    # popped_node.next = None
    # doing this so as to elimicate unutilised pointers, that might cause memory leak.

    def pop_first(self):
        """Removes the first element."""
        if self.head == None:
            return False
        popped_node = self.head
        if self.head == self.tail:
            self.head = None
            self.tail == None
        else:
            self.head = self.head.next
        popped_node.next = None
        self.length -= 1
        return True

    def pop(self):
        """removes the last element."""
        if self.head == None:
            return False
        popped_node = self.tail
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            current = self.head
            while current.next is not self.tail:
                current = current.next
            self.tail = current
            current.next = None
        popped_node.next = None
        self.length -= 1
        return True

    def remove(self, index):
        """Removes the node in index mentioned."""
        if index >= self.length or index < 0:
            return False
        if index == 0:
            self.pop_first()
        elif index == self.length - 1:
            self.pop()
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            popped_node = current.next
            current.next = current.next.next
            popped_node.next = None

            # # or - Even easily
            # prev_node = self.get(index-1)
            # popped_node = prev_node.next
            # prev_node.next = popped_node.next
            # popped_node.next = None

            self.length -= 1
            return True

    def delete_all(self):
        """removes all elements in the linked list."""
        # # or
        # self.head = None
        # self.tail = None
        # self.length = 0
        if self.head == None:
            return False
        current = self.head
        for _ in range(self.length):
            self.pop()


# # Created three nodes and saw their respective memory locations :
# node1 = Node(10)
# node2 = Node(11)
# node3 = Node(10)
# print(f" node 1 : {node1}\n\
#     node 2 : {node2} \n\
#         node 3 : {node3}")
new_ll = LinkedList()
new_ll.append(10)
new_ll.append(111)
new_ll.append(11)
new_ll.append(119)
new_ll.append(150)
new_ll.append(140)
new_ll.append(121)
new_ll.prepend(9)
new_ll.insert(12, 0)
new_ll.insert(13, 3)
print(new_ll)
print(new_ll.search(11))
print(new_ll.get(4).value)
new_ll.set(3, 18)
print(new_ll)
new_ll.pop_first()
print(new_ll)
new_ll.pop()
print(new_ll)
new_ll.remove(0)
print(new_ll)
new_ll.delete_all()
print(new_ll)
