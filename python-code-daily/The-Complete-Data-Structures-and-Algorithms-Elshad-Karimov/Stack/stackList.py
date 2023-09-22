class Stack : 
    """Creates a stack with build-in list data structure."""
    
    def __init__(self):
        self.list = []
        self.top = -1
        
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
          
    def push(self, value):
        """adds the value into the stack"""
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