#Zad 1

x=np.arange(1, 20, 1)
plt.plot(x, 1/x, 'g:^')
plt.axis([0,20,0,1])
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend(labels=['f(x)= 1/x'])
plt.show()
