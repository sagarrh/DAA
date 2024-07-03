import matplotlib.pyplot as mp
import numpy as np

a=np.random.rand(50)
b=np.random.rand(50)

mp.scatter(a,b,facecolors='none',edgecolors='y')
mp.xlabel('x')
mp.ylabel('y')
mp.title("scatter plot with random numbers")
mp.show()