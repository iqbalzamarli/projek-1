print("Program menulis file teks")
print("===========================")

nama = input("nama  :")
umur = input("umur  :")
alamat = input("Alamat  :")

teks = "nama : {}\nUmur :   {}\nAlamat : {}".format(nama,umur,alamat)

file_bio = open("biodata.txt","w")

file_bio.write(teks)

file_bio.close()