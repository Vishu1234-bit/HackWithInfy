m,n = map(int,input().split())
cm = int(input())
cn = int(input())
if(cm==cn):
    breaks=(((m*n)-1)*cm)
elif(cm >cn):
    breaks = ((m-1)*cm)+(((n-1)*cn)*m)
else:
    breaks = ((m-1)*cm)*n+((n-1)*cn)
print(breaks)
