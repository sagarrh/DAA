import numpy as np

array= np.array([[1,2,3,4],[2,3,4,5],[4,3,2,1]])
row_to_check=np.array([1,2,3,4])

def some(a,b):
    return (a==b).all(axis=1).any()

if contains_row(array,row_to_check):
    print