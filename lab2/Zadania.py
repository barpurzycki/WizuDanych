# Zad 1.

UlubSporty = ['piłka nożna', 'siatkówka', 'sztuki walki']
UlubSporty.reverse()
UlubSporty.insert(3, 'koszykówka')
print(UlubSporty)

# Zad 2.

Słownik = {"m.in": "między innymi", "itp.": "I tym podobne", "itd.": "I tak dalej"}

print(Słownik.keys())
print(Słownik.values())

# Zad 3.

SlowGry = {"Ulubiona seria": "Dark Souls", "Najnowsza ulubiona": "Elden Ring", "Sentyment": "Wiedźmin 3", "Największa ilość spędzonego czasu": "League of Legends"}
print(len(SlowGry.keys()))

# Zad 4.

zdanie = input("Podaj zdanie: ")
print(zdanie.count("a"))

# Zad 5.

import sys as system

a = system.stdin.readline()
a = int(a)
b = system.stdin.readline()
b = int(b)
c = system.stdin.readline()
c = int(c)

wynik = (a ** b) + c
wynik = str(wynik)
system.stdout.write(wynik)

# Zad 6.

a = input("Podaj pierwszą liczbę: ")
a = int(a)
b = input("Podaj drugą liczbę: ")
b = int(b)
c = input("Podaj trzecią liczbę: ")
c = int(c)

if (a > b) & (a > c):
    print("Pierwsza liczba jest największa")
elif (b > a) & (b > c):
    print("Liczba druga jest największa")
elif (c > a) & (c > b):
    print("Liczba trzecia jest największa")
else:
    print("Któraś z liczb jest równa innej")

# Zad 7.

ListaLiczb = [2, 4, 6, 7.5, 8.2]

for i in ListaLiczb:
    i = i ** 2
    print(i)

# Zad 8.

x = 1
x = int(x)
Lista = []

while x != 11:
    print(x)
    if (x % 2) == 0:
        Lista.append(x)
    x += 1

print("Lista: ")
print(Lista)

# Zad 9.

y = input("Podaj liczbę: ")
y = int(y)
try:
    pierw = math.sqrt(y)
    print(pierw)
except ValueError:
    print("Liczba nie może być ujemna")
