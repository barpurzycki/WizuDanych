import numpy as np

#Zad 1

a = np.arange(4, 84, 4)
print(a)

#Zad 2

a = np.arange(10, dtype='float')
print(a)
b = a.astype('int32')
print(b)

#Zad 3

def fun(n):
    x=np.zeros((pow(2,n),pow(2,n)))
    return x
print(fun(2))

#Zad 4

def generuj(liczba, ilosckol):
    wynik=np.logspace(1,ilosckol,num=ilosckol,base=liczba, dtype="int32")
    return wynik
print(generuj(2,4))

#Zad 5

def wektor(dlugosc):
    a=np.arange(dlugosc)
    odwrocony=a[::-1]
    macierz=np.diag([a for a in odwrocony],2)
    return macierz
print(wektor(3))

#Zad 6

wykreslanka=np.array([["d","o","m","w","t","k","w"],["q","s","t","w","x","o","h"],["n","d","x","k","g","s","r"]])
print(wykreslanka)

#Zad 7

def macierz(n):
    x=np.zeros((n,n))
    for y in range(0,n):
        for z in range(0,n):
            if(z>y):
                x[y,z]=abs(2*(z-y+1))
            else:
                x[y,z]=abs(2*(y-z+1))

    return x
print(macierz(3))

#Zad 8

def podzial(tablica,kierunek):
    if(kierunek=="poziomo" or kierunek=="pionowo"):
        if(tablica.shape[0]%2==1 and kierunek=="poziomo"):
            return "nie możesz tego zrobić, bo wysokość tablicy jest liczbą nieparzystą"
        if(tablica.shape[1]%2==1 and kierunek=="pionowo"):
             return "nie możesz tego zrobić, bo szerokość tablicy jest liczbą nieparzystą"
        else:
            if(kierunek=="poziomo" and tablica.shape[0]%2==0):
                tab1=np.zeros((tablica.shape[0]//2,tablica.shape[1]))
                tab2 = np.zeros((tablica.shape[0]//2, tablica.shape[1]))
                for i in range(0,tab1.shape[0]):
                    for j in range(0,tab1.shape[1]):
                        tab1[i,j]=tablica[i,j]
                for i in range(tab2.shape[0],tablica.shape[0]):
                    for j in range(tab2.shape[0], tablica.shape[0]):
                        tab2[i-tab2.shape[0], j-tab2.shape[0]] = tablica[i, j]
                return tab1,tab2
            if (kierunek == "pionowo" and tablica.shape[1] % 2 == 0):
                tab1 = np.zeros((tablica.shape[0], tablica.shape[1]//2))
                tab2 = np.zeros((tablica.shape[0], tablica.shape[1]//2))
                for i in range(0, tab1.shape[0]):
                    for j in range(0, tab1.shape[1]):
                        tab1[i, j] = tablica[i, j]
                for i in range(tab2.shape[0], tablica.shape[0]):
                    for j in range(tab2.shape[0], tablica.shape[0]):
                        tab2[i - tab2.shape[0], j - tab2.shape[0]] = tablica[i, j]
                return tab1, tab2


    else:
        return "nastepnym razem wpisz jako kierunek 'pionowo' lub 'poziomo'"


#Zad 9

r=input("podaj róznicę(int)")
a1=input("podaj 1 wyraz ciągu(int)")
r=int(r)
a1=int(a1)

list=[a1+r*i for i in range(0,25)]


macierz=np.zeros((5,5))
licznik=0
for i in range(0,5):
    for j in range(0,5):
        macierz[i,j]=list[licznik]
        licznik+=1

print(macierz)
