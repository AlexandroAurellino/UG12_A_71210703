a = input("Masukkan deret angka : ")
x = 0
y = (a.split(","))
print("Total :",end=" ")
for i in y:
    i=int(i)
    if i%2==1:
        x = x-i
        print(i*-1, end=" ")
    else:
        x = x+i
        print("+",i,end=" ")
print()
print("Hasil perhitungan diatas ialah", x)