#Zad 1

# lista = []
#
# for a in range(0, 31):
#     a = a * 2
#     lista.append(a)
#
# plik = open('zadania.txt', 'w+')
#
# plik.writelines(str(lista))
# plik.close()
#
#Zad 2
#
# plik = open('zadania.txt', 'r')
#
# odczyt = plik.readlines()
#
# print(odczyt)
# plik.close()

#Zad 3

# with open('zadania.txt', 'w') as plik:
#     for a in range(0, 10):
#         plik.write('Linijka tekstu \n')
#
# with open('zadania.txt', 'r') as plik:
#     for a in plik:
#         print(a, end='')

#Zad 4

# class NaZakupy:
#     def __init__(self, nazwa_produktu, ilosc, jednostka_miary, cena_jed):
#         self.nazwa_produktu=nazwa_produktu
#         self.ilosc=ilosc
#         self.jednostka_miary=jednostka_miary
#         self.cena_jed=cena_jed
#     def wyswietl_produkt(self):
#         print(self.nazwa_produktu)
#         print(self.ilosc)
#         print(self.jednostka_miary)
#         print(self.cena_jed)
#     def ile_produktu(self):
#         print(self.ilosc, self.jednostka_miary)
#     def ile_kosztuje(self):
#         return self.ilosc*self.cena_jed
#
# ziemniaki = NaZakupy("Ziemniaki", 3, "Kg", 2)
#
# ziemniaki.wyswietl_produkt()
# ziemniaki.ile_produktu()
# print(ziemniaki.ile_kosztuje())

#Zad 5

# class ciagAryt:
#     def __init__(self, a1, n, r):
#         self.a1=a1
#         self.n=n
#         self.r=r
#     def wyswietl_dane(self):
#         wyraz=self.a1
#         for x in range(self.n):
#             print(wyraz)
#             wyraz = wyraz + self.r
#     def pobierz_elementy(self, x, y, z):
#         self.a1=x
#         self.n=y
#         self.r=z
#     def pobierz_parametry(self):
#         self.a1 = int(input())
#         self.n = int(input())
#         self.r = int(input())
#     def policz_sume(self):
#         an=self.a1+(self.n-1)*self.r
#         suma=((self.a1+an)/2)*self.n
#         return suma
#
# ciag=ciagAryt(1,2,3)
# ciag.wyswietl_dane()
#
# ciag.pobierz_elementy(4,5,6)
# ciag.wyswietl_dane()
#
# ciag2 = ciagAryt(0, 0, 0)
# ciag2.pobierz_parametry()
# ciag2.wyswietl_dane()
#
# print(ciag.policz_sume())
# print(ciag2.policz_sume())

#Zad 6

# class Robaczek:
#     def __init__(self, x,y,krok=2):
#         self.x=x
#         self.y=y
#         self.krok=krok
#     def idz_w_gore(self, ile_krokow):
#         self.y+=self.krok*ile_krokow
#     def idz_w_dol(self, ile_krokow):
#         self.y-=self.krok*ile_krokow
#     def idz_w_lewo(self, ile_krokow):
#         self.x-=self.krok*ile_krokow
#     def idz_w_prawo(self, ile_krokow):
#         self.x+=self.krok*ile_krokow
#     def pokaz_gdzie_jestes(self):
#         print(self.x, self.y)

# robaczek=Robaczek(0,0)

# robaczek.idz_w_gore(2)

# robaczek.idz_w_dol(4)

# robaczek.idz_w_lewo(5)

# robaczek.idz_w_prawo(1)

# robaczek.pokaz_gdzie_jestes()
