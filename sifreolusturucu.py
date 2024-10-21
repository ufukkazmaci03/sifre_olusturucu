import random
karekterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

sayi = int(input("Şifreniz kaç karakterden oluşsun?"))
sifre = ""



for i in range(sayi):
    sifre += random.choice(karekterler)

print("Şifreniz:",sifre)
