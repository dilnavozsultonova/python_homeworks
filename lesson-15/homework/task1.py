import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(-10,10,1000)
y=x**2-4*x+4
plt.plot(x,y)
plt.title("Graph")
plt.xlabel("values")
plt.ylabel("Yvalues")
plt.show()