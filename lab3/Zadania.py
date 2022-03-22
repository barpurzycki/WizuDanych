#Zad 1

# A=[1-x for x in range(1, 11)]
# print(A)
# B=[4**x for x in range(0, 8)]
# print(B)
# C=[x for x in B if x%2==0]
# print(C)

#Zad 2

# import random
#
# lista1=[]
# for x in range(11):
#     lista1.append(random.randrange(1, 100))
# print(lista1)
# lista2=[x for x in lista1 if x%2==0]
# print(lista2)

#Zad 3

# prodspoz={'Woda':"Sztuki", "Pomidory":"Kg", "Kiełbasa":"KG","Bułka":"Sztuki"}
# print(prodspoz)
# prodspoz2={key:value for key, value in prodspoz.items() if value=="Sztuki"}
# print(prodspoz2)

#Zad 4

# def czyProstokatny(a, b, c):
#     if pow(a, 2) + pow(b, 2) == pow(c, 2):
#         print("Jest prostokątny")
#     else:
#         print("Nie jest prostokątny")
#
# czyProstokatny(3, 4, 5)

#Zad 5

# def poleTrap(a=1, b=2, h=3):
#     pole=((a+b)*h)/2
#     return pole
#
# print(poleTrap())

#Zad 6

# def ciag(a=1,b=4,ile=10):
#     for x in range(ile):
#         a=a*b
#     return a
#
# print(ciag())

#Zad 7

# def ciagop(*liczba):
#     if len(liczba)==0:
#         return 0
#     else:
#         iloczyn = 1
#         for x in liczba:
#             iloczyn=iloczyn*x
#     return iloczyn
#
# print(ciagop(1, 2, 3, 4, 5, 6, 7, 8))

#Zad 8

# def lista(**produkt):
#     cena=len(produkt.items())
#     paragon = 0
#     ileprod = 0
#     for key, value in produkt.items():
#         paragon += value
#         ileprod = len(produkt.keys())
#     return ileprod, paragon
# 
# print(lista(czekolada=5, chipsy=5.5 ))
