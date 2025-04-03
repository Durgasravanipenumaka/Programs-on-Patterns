n=int(input())
for i in range(0,n+1,+1):
    for j in range(0,n+1-i,+1):
        if j == n-i :
            print("*")
        else :
            print(end=" ")       