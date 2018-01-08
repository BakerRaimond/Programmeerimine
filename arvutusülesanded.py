#arvutus ülesanded
nimi = input("Palun sisesta oma nimi ja vajuta ENTER: ")
print("Tere " + nimi + "!")

a = float(input("Palun sisesta esimene arv: "))
b = float(input("sisesta teine arv: "))

print("arvude summa:", a + b)
print("arvude korrutis:", a * b)
print("Esimese ja teise jagatis:", a / b)
print("25% esimesest arvust:", a * 0.25)

if a == b:
    print("arvud on võrdsed")
else:
    print("arvud on erinevad")
    if a > b:
        print("Esimene arv on suurem")
    else:
        print("Teine arv on suurem")

from math import sin, cos, pi

print(pi)
print(cos(0.5))

x = sin(4)
print(x)

y = 123
print(round(x + y, 2))
