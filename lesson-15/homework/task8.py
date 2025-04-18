import numpy as np
import matplotlib.pyplot as plt

categories=["Category A", "Category B","Category C"]
T1 = np.random.randint(1,10,3)
T2 = np.random.randint(1,10,3) + T1
T3 = np.random.randint(1,10,3) + T2
T4 = np.random.randint(1,10,3) + T3


plt.title("Stacked bar chart")
plt.ylabel("categories")
plt.bar(categories, T4,label="T4")
plt.bar(categories, T3,label="T3")
plt.bar(categories, T2,label="T2")
plt.bar(categories, T1,label="T1")
plt.legend()

plt.show()