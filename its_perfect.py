n = int(input())
f= set([1])
if(n==1):
    print("NO")
i=2
while(i*i<=n):
    if(n%i==0):
        f.add(i)
        f.add(n//i)
    i+=1
if(sum(f)==n):
    print("yes")
else:
    print("no")
