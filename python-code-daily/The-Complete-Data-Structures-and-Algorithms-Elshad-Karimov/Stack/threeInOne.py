class MultiStack : 
    def __init__(self, stacksize):
        self.numberOfStacks = 3 # this is for the number of stacks to be present in one list.
        self.custList = [0] * (self.numberOfStacks * stacksize) # the complete list is represented as an list of 0's 
        self.sizes = [0] * self.numberOfStacks # this is the count of each stack in the list
        self.stacksize = stacksize # total stack size
        
    def isFull(self, stacknum) :
        if self.sizes[stacknum] == self.stacksize :
            return True
        else : 
            return False
        
    def isEmpty(self, stacknum) : 
        if self.sizes[stacknum] == 0 : 
            #print("True, empty!")
            return True
        else : 
            return False
    
    def topElementIndex(self, stacknum) :
        offset = stacknum * self.stacksize
        return offset + self.sizes[stacknum] - 1
    
    def push(self, stacknum,  element) :
        if self.isFull(stacknum) :
            return "Full!"
        self.sizes[stacknum] += 1
        self.custList[self.topElementIndex(stacknum)] = element 
        return "Pushed!"
    
    def pop(self, stacknum) :
        if self.isEmpty(stacknum) :
            return "Empty!"
        self.custList[self.topElementIndex(stacknum)] = 0 
        self.sizes[stacknum] -= 1
        return "Popped!"
    
    def peek(self, stacknum) :
        if self.isEmpty(stacknum) :
            return "Empty!"
        value = self.custList[self.topElementIndex(stacknum)]
        return f"Peek : {value}"
        

customStack = MultiStack(4) 
print(customStack.isFull(0))      
print(customStack.isEmpty(1))
print(customStack.push(1,0))
print(customStack.push(2,9))
print(customStack.push(2,4))
print(customStack.isEmpty(2))
print(customStack.peek(2))
print(customStack.pop(2))
print(customStack.peek(2))
    