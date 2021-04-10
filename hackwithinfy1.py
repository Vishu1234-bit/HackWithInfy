t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    a = [0 for i in range(0,1001)]
    for i in range(0,n-1):
        a[arr[i]]+=1
        if(arr[i]==arr[i+1]):
            i+=1
    for i in range(0,len(a)):
        if(a[i] == max(a)):
            out = i
            break
    print(out)
    

                
