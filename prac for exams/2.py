import matplotlib.pyplot as mp
import numpy as np

a=np.random.rand(50)
b=np.random.rand(50)

sizes=np.random.rand(50)*100

mp.scatter(a,b,sizes)
mp.xlabel('x')
mp.ylabel('y')
mp.title("scatter plot with balls of different sizes")
mp.show()