import random

karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
si_uz=int(input("şifre uzunluğu belirle:"))
sifre=""
for i in range(si_uz):
    sifre += random.choice(karakterler)
print(sifre)