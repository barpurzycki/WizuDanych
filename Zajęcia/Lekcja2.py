# a = 10
# b = 5
# if a == b:
#     print("Jest równe")
# elif a > b:
#     print("a większe od b")
# elif a < b:
#     print("b większe od a")
# elif a != b:
#     print("a jest różne od b")
# elif a >= b:
#     print("a jest większe lub równe b")
# elif a <= b:
#     print("a jest mniejsze lub równe b")
# else:
#     print("żadne z tych")


# a = input('wpisz liczbę: ')
# print(a)
# print(type(a))
#
# a = int(a)
# print(type(a))

# a = input('wpisz pierwszą liczbę: ')
# b = input('wpisz drugą liczbę: ')
# c = input('wpisz trzecią liczbę: ')
# d = input('wpisz czwartą liczbę: ')
#
# a=int(a)
# b=int(b)
# c=int(c)
# d=int(d)
#
# if (a > b) & (c > d):
#     print("Liczba a jest większa od liczby b i liczba c jest większa od liczby d")
# else:
#     print("Liczba a jest mniejsza od liczby b lub liczba c jest mniejsza od liczby d")

# for licznik in sekwencja:
#     instrukcja bądź blok instrukcji
# else:
#     instrukcje po wykonaniu pętli for

#range(start, stop, stop)
#for(int i = 0; i < 10; i++)

# for i in range(1, 7):
#     print(i)

# lista = ['a', 5, 6, 1, 2, 3.1]
# for a in lista:
#     print(a)
# else:
#     print("Wyświetlono wszystkie elementy")

# while warunek:
#     instrukcja lub blok instrukcji, gdy warunek spełniony
# else:
#     instrukcje po pętli

# i=0
# while i < 10:
#     print(i)
#     i+=1

# lista = [1, 2, 5, 7, 3, 4, 8]
# liczba = input('podaj liczbę: ')
# licznik = 0
# while licznik < len(lista):
#     if int(liczba) - lista[licznik] == 0:
#         print('liczba ' + str(liczba) + ' - ' + str(lista[licznik]) + ' = 0')
#         break
#     else:
#         licznik += 1
# else:
#     print('żadna z wartości nie dała wyniku')

# lista1 = [4, 2, 6, 3, 1]
# lista2 = [4, 7, 5, 2]
# suma = []
# for a in lista1:
#     for b in lista2:
#         wynik = a + b
#         suma.append(wynik)
#     print(suma)

# try:
#     instrukcje, które mogą zawierać błąd
# except nazwa błędu:
#     instrukcje po wykryciu błędu
# except nazwa błędu2:
#     instrukcje po wykryciu błędu
# .
# .
# .
# else:
#     wynik, gdy nie ma błędu

# a = input('podaj liczbe: ')
# b = input('podaj drugą liczbe: ')
# try:
#     a = int(a)
#     b = int(b)
#     wynik = a / b
#     print(wynik)
# except ZeroDivisionError:
#     print("Nie można dzielić przez 0")
# except ValueError:
#     print("Nie wpisano liczby całkowitej")

# lista = ['a', 5, 5, 5, [1, 2, 3]]
# słownik = {'klucz': 'wartość'}
# a = lista[nr_indeksu]
#
# print(słownik['nazwa_klucza'])
#
# do listy
# append, insert, extend
# pop, remove, del
# sort, reverse

# lista = [5, 1, 2, 6]
# print(lista)
# lista.append(7)
# print(lista)
# lista.insert(5, 9)
# print(lista)
# lista.extend([6, 1, 3])
# print(lista)
# lista.pop(3)
# print(lista)
# lista.remove(6)
# print(lista)
# del lista[0]
# print(lista)
# lista.sort()
# print(lista)
# lista.reverse()
# print(lista)

słownik = {'a': '40', 'b': '30', 'c': 'Trzecia wartość'}
print(słownik['c'])
