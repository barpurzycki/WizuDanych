import math
# lista = []
# for element in sekwencja
#     if warunek_na_element:
#         lista.append(akcja_na_element)
#     lista = [akcja na element for element in sekwencja if warunek na element]

# a = []
#
# for x in range(0, 10):
#     a.append(x**2)
# print(a)
#
# a1 = [x**2 for x in range(0, 10)]
# print(a1)
#
# b = []
#
# for x in range(0, 6):
#     b.append(3**x)
# print(b)
#
# b1 = [3**x for x in range(0, 6)]
# print(b1)
#
# c = []
# for x in a:
#     if x%2==1:
#         c.append(x)
# print(c)
#
# c1 = [x for x in a if(x%2==1)]
# print(c1)
#
# lista2= [a, b, c]
# print(lista2)

# lista = []
# for a in [1, 2, 3]:
#     for b in [4, 5, 6]:
#         lista.append((a, b))
# print(lista)
#
# lista2 = [(a, b) for a in [1, 2, 3] for b in [4, 5, 6]]
# print(lista2)

# słownik = {"PZU":"Państwowy zakład ubezpieczeń",
#            "ZUS":"Zakład ubezpieczeń społecznych",
#            "PKO":"Państwowa kasa oszczędności"}
# print(słownik)
# słownik_odwrocony={}
# for key, value in słownik.items():
#     słownik_odwrocony[value]=key
# print(słownik_odwrocony)
# słownik2 = {value:key for key, value in słownik.items()}
# print(słownik2)

# def nazwa_funkcji(arg pozycyjne, domyślne=wartość, *argument, **argument):
#     instrukcje
#
# return

# def row_kwadratowe(a, b, c):
#     delta = b**2 - 4 * a * c
#     if delta < 0:
#         print("Brak rozwiązań")
#         return -1
#     if delta == 1:
#         print("Jedno rozwiązanie")
#         x = (-b)/2*a
#         return x
#     else:
#         print("Dwa rozwiązania")
#         x1 = ((-b) - math.sqrt(delta))/2*a
#         x2 = ((-b) + math.sqrt(delta))/2*a
#         return x1, x2
#
# print(row_kwadratowe(1, 2, 3))
# print(row_kwadratowe(3, 6, 3))
# print(row_kwadratowe(2, 10, 3))
#
# def parzystosc(a):
#     if a%2==0:
#         return "Jest parzysta"
#     else:
#         return "Nieparzysta"
#
#
# print(parzystosc(9))
#
# print(parzystosc(10))

# def dlugosc_odcinka(x1=1, y1=2, x2=3, y2=4):
#     return math.sqrt((x2-x1)**2 + (y2-y1)**2)
#
# print(dlugosc_odcinka())
#
# print(dlugosc_odcinka(4, 5, 6, 9))
#
# print(dlugosc_odcinka(1, 2, y2=8, x2=10))
#
# print(dlugosc_odcinka(x2 = 5, y1 = 2, x1 = 3, y2 = 10))
#
# print(dlugosc_odcinka(x1 = 10, x2= 20))

# def ciag(*liczba):
#     if len(liczba)==0:
#         return 0
#     else:
#         suma = 0
#         for i in liczba:
#             suma += i
#         return suma
#
# print(ciag())
# print(ciag(1, 2, 3, 4, 5, 6, 7))


# def co_lubie(**rzeczy):
#     for cos in rzeczy:
#         print("Lubię")
#         print(cos)
#         print("Co lubię")
#         print(rzeczy[cos])
# 
# co_lubie(gry = ["Dark Souls", "Elden Ring"])
