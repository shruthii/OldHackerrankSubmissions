from itertools import product
list1= map(int,input().split(" "))
list2=map(int,input().split(" "))
print (" ".join(map(str,list(product(list1,list2)))))
