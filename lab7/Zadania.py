#Zad 1

a = np.arange(3)
b = np.arange(3)
print(a)
print(b)
print(a*b)

#Zad 2

a = np.arange(9).reshape(3,3)
b = np.arange(16).reshape(4,4)
print(a)
print(b)
print()
print(a.min(axis = 0))
print(a.min(axis = 1))
print()
print(b.min(axis = 0))
print(b.min(axis = 1))

#Zad 3

a = np.arange(3)
b = np.arange(3)
c = a.dot(b)
print(c)

#Zad 4

a = np.array([2, 4, 5, 6, 9])
b = np.array([2.5, 3, 1.5, 0.2, 1.5])
print(a*b)

#Zad 5/6/7

x = np.arange(6).reshape(2,3)
print(x)
a = np.sin(x)
print(a)
b = np.cos(x)
print(b)
print(a+b)

#Zad 8

a = np.arange(9).reshape(3,3)
for b in a:
    print(b)
    
#Zad 9

a = np.arange(9).reshape(3,3)
for b in a.flat:
    print(b)
    
#Zad 10

a = np.arange(81).reshape(9,9)
print(a)
print()
print()
b = a.T
print(b)
print()
print()
c = a.ravel()
print(c)
print()
print()
d = np.arange(81).reshape(3,27)
print(d)
print()
print()
e = np.arange(81).reshape(27,3)
print(e)
print()
print()
f = np.arange(81).reshape(1,81)
print(f)
print()
print()
g = np.arange(81).reshape(81,1)
print(g)

#Zad 11

a = np.arange(12)
print("wektor")
print(a)
print()
b = a.reshape(3,4)
print("macierz 3x4")
print(b)
print()
c = a.reshape(4,3)
print("macierz 4x3")
print(c)
print()
d = a.reshape(2,6)
print("macierz 2x6")
print(d)
print()

print("spłaszczony wektor")
for q in a.flat:
    print(q)
print("spłaszczona macierz 3x4")
for x in b.flat:
    print(x)
print("spłaszczona macierz 4x3")
for y in c.flat:
    print(y)
print("spłaszczona macierz 2x6")
for z in d.flat:
    print(z)
