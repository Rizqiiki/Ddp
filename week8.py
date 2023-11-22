def profil(Nama, Alamat, Umur, jk, Hobby):   
      print("Nama saya",Nama)
      print("Alamat saya",Alamat)
      print("Umur saya",Umur)
      print("Jenis kelamin saya",jk)
      print("Hobby saya",Hobby)

profil("Rizqi", "Depok", "21", "Laki-Laki", "Futsal")

def nilai(a):
     if ( a <=60):
         print("gagal")
     elif (a >= 61 and a <= 70):
         print("baik")
     elif ( a >= 71 and a <= 80):
         print("sangat baik")
     elif ( a >= 81 and a <= 100):
         print("istimewa")
     else:
        ("Masukan nilai yang benar")
nilai(80)

def cetak_ganjil(a):
    for i in range(1, 101, 2):
        print(i)

cetak_ganjil(100)