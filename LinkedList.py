    def insert(self,head,data): 
    #Complete this method
        if head == None: 
            head = Node(data)
            #print (head.data)
        else:
            curr= head
            while curr.next:
                curr = curr.next
            curr.next = Node(data)
            #print (curr.data)
        return head      
        
            