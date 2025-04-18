import numpy as np
import matplotlib.pyplot as plt
data=np.random.randn(1000)

plt.hist(data,bins=30,color="red",alpha=0.5,edgecolor="blue")
plt.title("Histogram")
plt.ylabel("Yvalues")
plt.xlabel("Xvalues")
plt.show()



