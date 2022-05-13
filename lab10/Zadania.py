import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import pandas as pd

#Zad 1

x=np.arange(1, 20, 1)
plt.plot(x, 1/x')
plt.axis([0,20,0,1])
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend(labels=['f(x)= 1/x'])
plt.show()

#Zad 2

x=np.arange(1, 20, 1)
plt.plot(x, 1/x, 'g:^')
plt.axis([0,20,0,1])
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend(labels=['f(x)= 1/x'])
plt.title("wykres funkcji f(x) dla x [1,20]")
plt.show()
         
#Zad 3

x = np.arange(0, 30, 0.1)
sin = np.sin(x)
cos = np.cos(x)
plt.plot(x, sin, label="sin(x)")
plt.plot(x, cos, label="cos(x)")
plt.legend(loc='upper left')
plt.xlabel("x")
plt.ylabel("sin(x) i cos(x)")
plt.show()
