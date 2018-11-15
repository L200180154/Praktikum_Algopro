b = str(input('Masukkan nama anda:'))
c = float(input('sekarang pukul :'))
if 00.00 <= c <= 11.59:
    print('selamat pagi', b)
elif 12.00 <= c <= 14.59:
    print('selamat siang', b)
elif 15.00 <= c <= 18.59:
    print('selamat sore', b)
elif 19.00 <= c <= 23.59:
    print('selamat malam', b)
