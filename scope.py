	# Add your code here
    #maximumDifference = 0
    def computeDifference(self):
        #pass
        self.maximumDifference = 0
        b =[]
        diff=0
        i=0
        j=0
        #print("hi")
        for i in range(0,len(self._Difference__elements)):
           #print("hi")
           #print(self._Difference__elements)
            for j in range (i+1,len(self._Difference__elements)):
                #print (self._Difference__elements[i])
                #print (self._Difference__elements[j])
                diff=abs(self._Difference__elements[i]-self._Difference__elements[j])
                #print (diff)
                b.append(diff)
        #print (b)
        self.maximumDifference = max(b)   
        #return self.maximumDifference  
         
        