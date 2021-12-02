x = str(input("Masukkan nama: "))
sutesna = []    #sutesna = nomer kursi
bambang = []    #bambang = daftar nama
while  x != "STOP":   
    g = "Masukkan nomor kursi "+x+" : "
    y = input(g)
    if y not in sutesna:
        sutesna.append(y)
        bambang.append(x)
    else:
        print("Mohon maaf kursi tersebut telah terisi!")
    x = str(input("Masukkan nama: "))
print("List kursi yang telah terisi :")
for i in range (len(sutesna)):
    print("Kursi nomor %s telah diisi oleh %s"%(sutesna[i],bambang[i]))
