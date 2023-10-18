# Meminta pengguna untuk memasukkan bilangan bulat positif
bilangan = int(input("Masukkan bilangan bulat positif: "))

# Mengecek apakah bilangan valid
if bilangan < 0:
    print("Masukkan bilangan bulat positif.")
else:
    faktor = []
    for i in range(1, bilangan + 1):
        if bilangan % i == 0:
            faktor.append(i)
    
    print("Faktor dari", bilangan, "adalah:", faktor)
