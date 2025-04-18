import numpy as np
import matplotlib.pyplot as plt

fig=plt.figure()
ax=plt.axes(projection="3d")

x=np.linspace(-5,5,100)
y=np.linspace(-5,5,100)

xx,yy=np.meshgrid(x,y)

zz = np.cos((xx**2 + yy**2))

ax.plot_surface(xx, yy, zz, cmap='Blues')
plt.show()

