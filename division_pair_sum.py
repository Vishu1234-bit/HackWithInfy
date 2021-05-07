t=int(input())
for i in range(t):
    arr = list(map(int,input().split()))
    m=int(input())
    freqmod = {}
    for num in arr:
        curr_rem = num%m
        if curr_rem in freqmod:
            freqmod[curr_rem]+=1
        else:
            freqmod[curr_rem]=1
    numpairs=0
    for rem in freqmod:
        comp  = m-rem
        pairs=0
        if comp==m or(2*comp==m):
             pairs = (freqmod[rem]*(freqmod[rem]-1))//2
        elif comp in freqmod:
             pairs=freqmod[rem]*freqmod[comp]
             freqmod[rem]=0
        numpairs = numpairs+pairs   
    print(numpairs)
