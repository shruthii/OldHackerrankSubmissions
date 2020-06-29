if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr1= list(arr)
    a=max(arr1)
    while(max(arr1)==a):
        arr1.remove(a)
    print (max(arr1))    
    