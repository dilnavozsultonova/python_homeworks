import numpy as np
import matplotlib.pyplot as plt
x = np.random.uniform(low=1,high=10,size=100)
y = np.random.uniform(low=1,high=10,size=100)
plt.title("Scatterplot")
plt.xlabel("values")
plt.ylabel("Yvalues")
plt.scatter(x,y,color="red")
plt.grid(True)

plt.show()