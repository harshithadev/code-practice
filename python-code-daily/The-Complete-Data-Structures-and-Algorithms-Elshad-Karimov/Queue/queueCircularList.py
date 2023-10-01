class Queue :
    """implementing queue data structure using lists"""
    
    def __init__(self, maxSize):
        self.top = -1
        self.start = -1
        self.maxSize = maxSize
        self.stack = [None] * maxSize 
        
    def __str__(self):
        result = ""
        if self.isEmpty():
            return False
        else : 
            result = f" < {self.stack[self.start]}"
            index = ( self.start+1 ) % self.maxSize
            while (index != self.start) : 
                result += f" < {self.stack[index]}"
                if index == self.top :
                    break
                
                index = ( index + 1 ) % self.maxSize
                
                
        return result
    
    def isEmpty(self):
        if self.top == -1   :
            return True
        else : 
            return False 
        
    def isFull(self):
        if ( self.start == 0 and self.top == ( self.maxSize - 1 ) ) or \
            ( self.start -1 == self.top ) :
                return True 
        else : 
            return False
    
    def enqueue(self,value):
        # if self.isEmpty():
        #     self.front = 0
        if self.isFull() :
            return False
        
        else : 
            if self.top+1 == self.maxSize : 
                self.top = 0
            else : 
                self.top += 1
                if self.start == -1 : 
                    self.start = 0 
        self.stack[self.top] = value
        
    def dequeue(self):
        if self.isEmpty():
            return False 
        else :
            if self.start == self.top : 
                self.start = -1
                self.top =  -1
            elif self.start + 1 == self.maxSize: 
                self.start = 0 
            else : 
                self.start += 1
    
    def peek(self):
        if self.isEmpty():
            return False 
        else :
            return self.stack[0]  
    
    def delete_all(self):
        self.top = -1
        self.start = -1
        self.stack = [None] * self.maxSize 
        
        
queque1 = Queue(6)  
print(queque1.isEmpty()) 
queque1.enqueue(10)
queque1.enqueue(11)
queque1.enqueue(12)
queque1.enqueue(13)
queque1.enqueue(14)
#queque1.enqueue(15)
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