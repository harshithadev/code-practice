class Node : 
    """Each node in a stack"""
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList : 
    def __init__(self):
        self.head = None
        self.length = 0


class Stack : 
    """Creates an empty stack."""
    def __init__(self):
        self.LinkedList = LinkedList()
        
    def __str__(self):
        result = ''
        temp_node = self.LinkedList.head
        while(temp_node is not None):
            result += f"{temp_node.value}"
            temp_node = temp_node.next
            if temp_node is not None : 
                result += "\n"
        return result
                
    def isEmpty(self):
        if self.LinkedList.head is not None : 
            return False 
        else : 
            return True
                
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.LinkedList.head
        self.LinkedList.head = new_node 
        self.LinkedList.length += 1
        
    def pop(self):
        #incase of empty stack
        if self.isEmpty() : 
            return False
        
        #else 
        popped_node = self.LinkedList.head 
        self.LinkedList.head = self.LinkedList.head.next
        popped_node.next = None
        self.LinkedList.length -= 1
    
    def peek(self):
        #incase of empty stack 
        if self.isEmpty(): 
            return False 
        #else 
        return self.LinkedList.head.value
    
    def delete_all(self): 
        self.LinkedList.head = None
        self.LinkedList.length = 0
        
        
stack1 = Stack()  
print(stack1.isEmpty()) 
stack1.push(10)
stack1.push(11)
stack1.push(12)
stack1.push(13)
stack1.push(14)
stack1.push(15)
print(stack1.isEmpty()) 
print(f"Peek : {stack1.peek()}")
stack1.pop()
stack1.pop()
stack1.pop()
stack1.pop()
stack1.pop()
stack1.pop()
print(stack1.pop())
print(stack1.isEmpty()) 
stack1.push(13)
stack1.push(14)
stack1.push(15)
print(stack1)
        
        
        
        
        
        
        
        
        
        
        
        
    
            