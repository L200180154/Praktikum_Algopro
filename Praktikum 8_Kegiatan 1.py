d = {
    "NIM" : "L200180154",
    "Nama" : "Aditya Dicky K",
    "Alamat" : "Jl.Kahuripan No.37A, Sumber",
    "No HP" : "082133100117",
    "Hobby" : "Futsal",
    "Universitas" : "Universitas Muhammadiyah Surakarta",
    "Jurusan" : "Informatika",
    }

def data1():
    print ("NIM: " + d["NIM"])
    return;
def data2():
    print ("Nama: " + d["Nama"])
    return;
def data3():
    print ("Alamat: " + d["Alamat"])
    return;
def data4():
    print ("No HP: " + d["No HP"])
    return;
def data5():
    print ("Hobby: " + d["Hobby"])
    return;
def data6():
    print ("Universitas: " + d["Universitas"])
    return;
def data7():
    print ("Jurusan: " + d["Jurusan"])
    return;

print ("""Pilihan yang tersedia:
               b menampilkan bantuan ini
               a menampilkan NIM
               c menampilkan Nama
               d menampilkan Alamat
               e menampilkan No HP
               f menampilkan Hobby
               g menampilkan Universitas
               h meanmpilkan Jurusan""")
x = "s"
while x != "k":
    x = str(input("Masukan Pilihan: "))
    if x == "b":
        print ("""Pilihan yang tersedia:
               b menampilkan bantuan ini
               a menampilkan NIM
               c menampilkan Nama
               d menampilkan Alamat
               e menampilkan No HP
               f menampilkan Hobby
               g menampilkan Universitas
               h meanmpilkan Jurusan""")
    elif x == "a":
        print("Pilihan saudara: a")
        data1()
    elif x == "c":
        print("Pilihan saudara: c")
        data2()
    elif x == "d":
        print("Pilihan saudara: d")
        data3()
    elif x == "e":
        print("Pilihan saudara: e")
        data4()
    elif x == "f":
        print("Pilihan saudara: f")
        data5()
    elif x == "g":
        print("Pilihan saudara: g")
        data6()
    elif x == "h":
        print("Pilihan saudara: h")
        data7()
    elif x == "k":
        print("Keluar")
    else:
        print("Pilihan tidak dikenali")
