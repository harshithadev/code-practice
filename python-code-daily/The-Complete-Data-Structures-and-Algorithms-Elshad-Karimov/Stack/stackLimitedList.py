class Stack : 
    """Creates a stack with build-in list data structure with a max limit."""
    
    def __init__(self, maxSize):
        self.list = []
        self.top = -1
        self.maxSize = maxSize
        
    def __str__(self):
        if self.isEmpty():
            return ""
        return "\n".join([str(x) for x in reversed(self.list)])

    def isEmpty(self): 
        if self.list == [] : 
            return True 
        else :
            return False 
        # or 
        # if len(self.list) == 0 : 
        #     return True 
        # else : 
        #     return False
    def isFull(self):
        if self.top + 1 == self.maxSize :
            return True
        else :
            return False  
                  
    def push(self, value):
        """adds the value into the stack"""
        if self.isFull() :
            return False
        
        self.top += 1
        self.list.append(value)
            
    def pop(self):
        """removes the top item from the stack"""
        if self.isEmpty() : 
            return False
        self.list.pop(self.top)
        self.top -= 1
            
    def peek(self) :
        if self.isEmpty() : 
            return False 
        else : 
            return self.list[self.top]        
    
    def deleteStack(self) : 
        del self.list
        #or 
        # #self.list = []
        
        
stack1 = Stack(10)
#print(stack1)
stack1.push(101)
#print(stack1)
stack1.push(10)
stack1.push(11)
stack1.push(12)
stack1.pop()
print(stack1.peek())
print(stack1.isEmpty())
print(stack1)
stack1.deleteStack()
print(stack1)