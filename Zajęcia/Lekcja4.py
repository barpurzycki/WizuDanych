# from teksty import *
#
# napis = 'dziś jest piątek'
# litery.wyswietl(napis)
# print(litery.dlugosc(napis))
# print(dodawanie.dodaj(4, 10))

# plik = open('tekst.txt', 'r')
# #wczytanie 10 znaków
# znaki = plik.read(10)
# #wczytanie linii
# wiersz = plik.readline()
# #wczytanie reszty pliku
# linie = plik.readlines()
#
# plik.close()
#
# print(znaki)
# print(wiersz)
# print(linie)

import sys

# print('Podaj kierunek studiów, rok i specjalizację')
# dane = sys.stdin.readline()
# plik = open('dane.txt', 'w+')
# plik.write(dane)
# plik.close()
#
# lista = []
# for a in range(7):
#     lista.append(a)
#
# plik = open('dane.txt', 'a+')
# plik.writelines(str(lista))
# plik.close()

# with open('tekst.txt', 'r') as plik:
#     for linia in plik:
#         print(linia, end='')

# class PierwszaKlasa:
#     """Pierwsza klasa python"""
#     atrybut = 54321
#     def pierwsza_metoda(self):
#         return 'pierwsza metoda w klasie'
#
# obiekt = PierwszaKlasa()
# print(obiekt)
# print(obiekt.atrybut)
# print(obiekt.pierwsza_metoda())
# obiekt.teskt = 'aaa'
# print(obiekt.teskt)

# class Ksztalty:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.opis = 'To będzie klasa dla ogólnych kształtów'
#
#     def pole(self):
#         return self.x * self.y
#
#     def obwod(self):
#         return 2 * self.x + 2 * self.y
#
#     def dodaj_opis(self, text):
#         self.opis = text
#
#     def skalowanie(self, czynnik):
#         self.x = self.x * czynnik
#         self.y = self.y * czynnik
#
# prostokat = Ksztalty(10, 30)
# print(prostokat.pole())
# print(prostokat.obwod())
# prostokat.dodaj_opis('Prostokąt')
# print(prostokat.opis)
# prostokat.skalowanie(0.5)
# print(prostokat.x)
# print(prostokat.y)
