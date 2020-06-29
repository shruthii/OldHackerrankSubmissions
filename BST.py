    def getHeight(self,root):
        #Write your code here
        count =0
        count1=0
        #print (root.data)
        while (root.left!= None and root.right!=None):
            root1=root
            if (root.left is not None):
                while(root is not None and (root.left is not None or root.right is not None)):
                    #print (type(root))
                    count = count+1
                    if root.left is not None :
                        root= root.left
                    else:
                        root=root.right
                    #print (root.data)
                    #print (count)
            if (root1.right != None):
                while(root is not None and (root1.left is not None or root1.right is not None)):
                    count1= count1+1
                    if root1.right is not None:
                        root1=root1.right
                    else:
                        root1=root1.left
                    #print (root1.data)
                    #print (count1)
        return max(count,count1)
                
            