n = input()
carry=0
total=0
i=len(n)-1
while(i>0):
    cur_dist = 10-int(n[i])+carry
    total=total+cur_dist
    carry=1
    i-=1
total=total+9
print(total)
    
