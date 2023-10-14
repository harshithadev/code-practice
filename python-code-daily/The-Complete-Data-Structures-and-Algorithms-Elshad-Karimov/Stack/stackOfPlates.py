# write solution using python lists.

class StackOfPlates : 
    def __init__(self, maxCapacity) :
        self.maxCapacity = maxCapacity
        self.stacks = [] 
        
    def isEmpty(self):
        if self.stacks == []:
            return True 
        else : 
            return False 
    
    def push(self, element) : 
        if len(self.stacks) > 0 and len(self.stacks[-1] < self.maxCapacity) :
            self.stacks[-1].append(element)
        else : 
            self.stacks.append([element])
            
    def pop(self) : 
        if len(self.stacks) == 0 : 
            return "Empty"
        else : 
            self.stacks[-1].pop()
            if len(self.stacks[-1]) == 0 :
                self.stacks.pop()
    
    def popAt(self, stackNumber) :
        self.stacks[stackNumber].pop()
    