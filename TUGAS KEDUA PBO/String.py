import re

def validasi_email(email):
    # Pola regex untuk validasi alamat email
    pattern = r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    
    # Memeriksa apakah alamat email sesuai dengan pola
    if re.match(pattern, email):
        return True
    else:
        return False

# Meminta pengguna memasukkan alamat email
email = input("Masukkan alamat email: ")

# Memanggil fungsi validasi_email untuk memeriksa alamat email
if validasi_email(email):
    print("Alamat email valid.")
else:
    print("Alamat email tidak valid.")
