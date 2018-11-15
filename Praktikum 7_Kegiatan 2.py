a = str(input("Masukkan password:"))
y = ('Aditya')
for x in range (3):
    if a == y:
        print('password benar')
        break
    elif a !=y:
        a = str(input('Maaf, anda salah memasukkan password. Masukkan password:'))
print('anda telah mencoba 3 kali. akses anda ditolak')
