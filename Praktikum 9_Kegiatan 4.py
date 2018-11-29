import shelve
a = open("L200180154.txt", "r")
NIM = a.readline()
Tanggal_Lahir = a.readline()
Nama = a.readline()
Kota = a.readline()
a.close()

a = shelve.open("Aditya")
a["b"] = [NIM, Tanggal_Lahir, Nama, Kota]
print(a["b"][0])
print(a["b"][1])
print(a["b"][2])
print(a["b"][3])
a.close
