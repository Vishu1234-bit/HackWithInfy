h = int(input())
w = int(input())
h1 = int(input())
w1 = int(input())
fold = 0
while(h!=h1 & w!=w1):
   while(h>h1):
      if((h/2)>=(h-h1)):
          h=h-(h-h1)
          fold = fold+1
      else:
          h = h/2
          fold = fold+1
  while(w>w1):
      if((w/2)>=(w-w1)):
          w=w-(w-w1)
          fold = fold+1
      else:
          w = w/2
          fold=fold+1
print(fold)
