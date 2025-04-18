import numpy as np
import matplotlib.pyplot as plt 
categories=['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
values=[200, 150, 250, 175, 225]
colors = ['red', 'blue', 'green', 'purple','green']
widths = [0.2,0.4, 0.6, 0.8, 1.0]

plt.bar(categories,values,color=colors,width=widths,edgecolor=["blue","red","purple","green","green"])
plt.title("products")
plt.xlabel("values")
plt.ylabel("categories")
plt.show()