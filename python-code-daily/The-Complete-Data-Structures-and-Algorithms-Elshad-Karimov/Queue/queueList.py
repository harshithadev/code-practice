class Queue :
    """implementing queue data structure using lists"""
    
    def __init__(self):
        #self.front = -1
        #self.rear = -1
        self.stack = []
        
    def __str__(self):
        result = ""
        if self.isEmpty():
            return False
        
        return " < ".join([str(x) for x in self.stack])
    
    def isEmpty(self):
        if self.stack == []:
            return True
        else : 
            return False 
    
    def enqueue(self,value):
        # if self.isEmpty():
        #     self.front = 0
        self.stack.append(value)
        
    def dequeue(self):
        if self.isEmpty():
            return False 
        else :
            return self.stack.pop(0)
    
    def peek(self):
        if self.isEmpty():
            return False 
        else :
            return self.stack[0]  
    
    def delete_all(self):
        self.stack = []
        
        
queque1 = Queue()  
print(queque1.isEmpty()) 
queque1.enqueue(10)
queque1.enqueue(11)
queque1.enqueue(12)
queque1.enqueue(13)
queque1.enqueue(14)
queque1.enqueue(15)
print(queque1.isEmpty()) 
print(f"Peek : {queque1.peek()}")
queque1.dequeue()
queque1.dequeue()
queque1.dequeue()
queque1.dequeue()
queque1.dequeue()
queque1.dequeue()
print(queque1.dequeue())
print(queque1.isEmpty()) 
queque1.enqueue(13)
queque1.enqueue(14)
queque1.enqueue(15)
print(queque1)