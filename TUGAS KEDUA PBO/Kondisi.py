import tkinter as tk

# Daftar nama bulan
bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]

# Daftar nama hari
hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]

# Fungsi untuk menampilkan hasil
def tampilkan_hasil():
    angka_bulan = int(entrada_bulan.get())
    angka_hari = int(entrada_hari.get())
    
    if 1 <= angka_bulan <= 12 and 0 <= angka_hari <= 6:
        nama_bulan = bulan[angka_bulan - 1]
        nama_hari = hari[angka_hari]
        hasil.config(text="Bulan {} adalah {} dan hari {} adalah {}.".format(angka_bulan, nama_bulan, angka_hari, nama_hari))
    else:
        hasil.config(text="Angka bulan atau angka hari tidak valid. Pastikan angka bulan dalam rentang 1-12 dan angka hari dalam rentang 0-6.")

# Membuat jendela Tkinter
root = tk.Tk()
root.title("Konversi Angka Bulan dan Hari")

# Mengatur warna latar belakang jendela
root.configure(bg='blue')

# Label dan Entry untuk angka bulan
label_bulan = tk.Label(root, text="Masukkan angka bulan (1-12):", bg='lightgray')
label_bulan.pack()
entrada_bulan = tk.Entry(root)
entrada_bulan.pack()

# Label dan Entry untuk angka hari
label_hari = tk.Label(root, text="Masukkan angka hari (0-6):", bg='lightgray')
label_hari.pack()
entrada_hari = tk.Entry(root)
entrada_hari.pack()

# Tombol untuk menampilkan hasil
tombol = tk.Button(root, text="Tampilkan", command=tampilkan_hasil)
tombol.pack()

# Label untuk menampilkan hasil
hasil = tk.Label(root, text="", bg='lightgray')
hasil.pack()

root.mainloop()
