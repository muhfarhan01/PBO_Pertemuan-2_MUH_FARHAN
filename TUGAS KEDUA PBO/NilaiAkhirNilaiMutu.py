nama="muhamad farhan"
nilai_kehadiran=100
nilai_tugas=90
nilai_uts=80
nilai_uas=80
nilai_akhir=int(0.10*nilai_kehadiran)+(0.20*nilai_tugas)+(0.30*nilai_uts)+(0.40*nilai_uas)

if(nilai_akhir>=85):
     nilai_mutu='A'
elif(nilai_akhir>=75):
     nilai_mutu='B'
elif(nilai_akhir>=55):
     nilai_mutu='C'
elif(nilai_akhir>=40):
     nilai_mutu='D'
else:
     nilai_mutu='E'
print(nilai_akhir)
print(nilai_mutu)