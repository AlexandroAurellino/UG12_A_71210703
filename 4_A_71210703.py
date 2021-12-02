n = int(input("input: "))
x = 2

for a in range(1,n+1):                  #a = mencari baris
    for b in range(1,(2*n)):            #b = mencari kolom
        if a+b==n+1 or b-a==n-1:
            print("*",end="")
        elif a==n and b!=x:
            print("*",end="")
            x=x+2
        else:
            print(end=" ")
    print()