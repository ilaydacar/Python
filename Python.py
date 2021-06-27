# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 18:56:14 2021

@author: ilayda
"""

print("""
************************
Kullanıcı Giriş Programı
************************
""")

sys_kul_adı = "ılaydaa"

sys_parola  = "12345" 

giriş_hakkı = 3
while True: 
    kullanıcı_adı = input("Kullanıcı Adı:")
    parola = input("Parola:")

    if (kullanıcı_adı != sys_kul_adı and parola == sys_parola):
        print("Kullanıcı Adı Hatalı")
        giriş_hakkı -= 1
        print("Giriş Hakkı: ", giriş_hakkı)
   
    elif (kullanıcı_adı == sys_kul_adı and parola != sys_parola):
        print("Parola Hatalı")
        giriş_hakkı -= 1
        print("Giriş Hakkı: ", giriş_hakkı)
   
    elif (kullanıcı_adı != sys_kul_adı and parola != sys_parola):
        print("Kullanıcı Adı ve Parola Hatalı...")
        giriş_hakkı -= 1
        print("Giriş Hakkı: ", giriş_hakkı)
        
    else:
        print("Başarıyla Giriş Yaptınız")
        break
    if (giriş_hakkı == 0 ):

        print("Giriş Hakkınız Bitti")
        break