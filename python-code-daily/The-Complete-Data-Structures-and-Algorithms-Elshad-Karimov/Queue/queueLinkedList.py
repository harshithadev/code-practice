class Node : 
    def __init__(self,value):
        self.value = value
        self.next = None
        
class LinkedList :
    def __init__(self):
        self.start = None
        self.top = None 
        self.length = 0

class Queue : 
    def __init__(self):
        self.linkedList = LinkedList()
        
    def __str__(self):
        result = ""
        current_node = self.linkedList.start
        while(current_node is not None) :
            result += f"{current_node.value}"
            if current_node.next is not None : 
                result += " < "
            current_node = current_node.next
        return result
    
    def isEmpty(self):
        if self.linkedList.start is None :
            return True 
        else : 
            return False 
    
    def enqueue(self, value):
        new_node = Node(value)
        if self.isEmpty() : 
            self.linkedList.start = new_node
            self.linkedList.top = new_node
        else : 
            self.linkedList.top.next = new_node
            self.linkedList.top = new_node
        self.linkedList.length += 1
            
    def dequeue(self):
        if self.isEmpty():
            return False
        popped_node = self.linkedList.start 
        if self.linkedList.start == self.linkedList.top :
            self.linkedList.start = None
            self.linkedList.top = None
        else :
            self.linkedList.start = self.linkedList.start.next 
        popped_node.next = None
        self.linkedList.length -= 1
    
    def peek(self):
        if self.isEmpty():
            return False 
        else : 
            return self.linkedList.start.value
        
    def delete_all(self):
        self.linkedList.start = None
        self.linkedList.top = None
        self.linkedList.length = 0
        

queque1 = Queue()
print(queque1.isEmpty()) 
queque1.enqueue(10)
queque1.enqueue(11)
queque1.enqueue(12)
queque1.enqueue(13)
queque1.enqueue(14)
print(queque1.linkedList.length)
print(queque1)  
#queque1.enqueue(15)
print(queque1.isEmpty()) 
print(f"Peek : {queque1.peek()}")
queque1.dequeue()
queque1.dequeue()
queque1.dequeue()
print(queque1.linkedList.length)
queque1.dequeue()
queque1.dequeue()
queque1.dequeue()
print(queque1.dequeue())
print(queque1.isEmpty()) 
queque1.enqueue(13)
queque1.enqueue(14)
queque1.enqueue(17)
queque1.enqueue(15)
print(queque1)