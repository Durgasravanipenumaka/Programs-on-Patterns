n=5

for i in range(1,n):
    spaces=2
    if i==1:
        print(" "*(n-i)+"*")
    elif i==n:
        print("* "*n)

    else:
        print(" "*(n-i-1)+"*"+" "*(spaces)*(i-1) +"* ")
  