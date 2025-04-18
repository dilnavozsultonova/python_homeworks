import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,10,100)
y=np.sin(x)
y1=x**3
y2=np.exp(x)
y3=np.log(x+1)
plt.subplot(2,2,1)
plt.plot(x,y1,color="red")
plt.title("graph")
plt.ylabel("Yvalues")
plt.subplot(2,2,2)
plt.plot(x,y,color="blue")
plt.title("graph")
plt.ylabel("Yvalues")
plt.subplot(2,2,3)
plt.plot(x,y2,color="green")
plt.title("graph")
plt.ylabel("Yvalues")
plt.subplot(2,2,4)
plt.plot(x,y3,color="yellow")
plt.title("graph")
plt.ylabel("Yvalues")
plt.show()



