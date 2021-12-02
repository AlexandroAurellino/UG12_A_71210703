x = input("Input : ")
y = len(x)
print("Output :",end="")
for i  in range(y):
    print(x[:i])
for j in range(y,0,-1):
    print(x[:j])