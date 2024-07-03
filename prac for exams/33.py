import numpy as np

a=np.array(['python','is','easy'])

array_with_spaces=np.array([' '.join(word) for word in a])

print(array_with_spaces)