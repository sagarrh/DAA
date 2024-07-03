import matplotlib.pyplot as mp
import numpy as np
math_marks= [88, 92, 80, 89, 100, 80, 60, 100, 80, 34]
sci_marks= [35, 79, 79, 48, 100, 88, 32, 45, 20, 30]
marks_range= [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

mp.scatter(math_marks,marks_range,color='blue',label='mathematics')
mp.scatter(sci_marks,marks_range,color='red',label='Science')

mp.xlabel('marks range')
mp.ylabel('marks scored')
mp.title("scatter plot of maths and science marks")
mp.legend()
mp.show()
