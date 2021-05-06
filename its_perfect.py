n = int(input())
f= []
for i in range(1,n):
    if(n%i==0):
        f.append(i)
if(sum(f)==n):
    print("yes")
else:
    print("no")
