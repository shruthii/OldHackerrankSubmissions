    def levelOrder(self,root):
        #Write your code here
        record = [root] if root else []
        while record:
            node=record.pop()
            print (node.data,end=" " )
            if node.left: record.insert(0,node.left)
            if node.right: record.insert(0,node.right)
            
            
               
            
            