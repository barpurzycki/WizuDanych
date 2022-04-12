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
