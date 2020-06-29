class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        sumlist =[]
        for i in range(1,n+1):
            if n%i ==0:
                sumlist.append(i)        
        return sum(sumlist)
    
                