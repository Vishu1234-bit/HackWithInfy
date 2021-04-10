t = int(input())
for i in range(t):
    a,b,c,x,y = map(int,input().split())
    chosen_pile = max(a,b,c)
    piles = [a,b,c]
    piles.remove(chosen_pile)
    pile1 = piles[0]
    pile2 = piles[1]
    if(x>=pile1 and y>=pile2):
       if((x-pile1)+(y-pile2) == chosen_pile):
             print("YES")
       else:
             print("NO")
    else:
        print("NO")
