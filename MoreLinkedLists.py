    def removeDuplicates(self,head):
        #Write your code here
        current = head
        if not head:
            return head
        while current.next:
            if current.data == current.next.data:
                current.next = current.next.next                
            else:
                current = current.next
        return head        
                
#         while head:
#             if queue.count(head.data)>1:
#                head1 = queue.pop()
#                #print("hi")
#             head = head.next
#             if head:
#                 queue.append(head.data)
       
#         for x in queue:
#             print (x,end=" ")
            
            
  
  
  
  
  
  
  
  
  