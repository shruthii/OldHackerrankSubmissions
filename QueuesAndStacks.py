class Solution:
    # Write your code here  
    def __init__(self):
        self.mystack = []
        self.myqueue = []
        
    def pushCharacter(self,j):
            #mystack = []   
        self.mystack.append(j)
        #print (mystack)
    def enqueueCharacter(self,j):
        #myqueue = []
        self.myqueue.append(j)
    def popCharacter(self):
        return self.mystack.pop()
    def dequeueCharacter(self):
        return self.myqueue.pop(0)
        
    