n=int(input())
for i in range(0,n+1,+1):
   for j in range(0,i,+1):
    print("*",end=" ")
   print("\n")
   if i==n:
      for i in range(n,0,-1):
        for j in range(i,0,-1):
          print("*",end=" ")
        print("\n")    