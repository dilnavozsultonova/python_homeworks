import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,2*np.pi,100)
y1=np.cos(x)
y2=np.sin(x)
plt.plot(x,y1,color="blue",linestyle="dashed",marker=">",label="cos")
plt.plot(x,y2,color="red",linestyle="dotted",marker="<",label="cos")
plt.legend()
plt.show()