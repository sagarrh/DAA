import numpy as np

mat1=np.array([[1,2,3],[4,5,6],[7,8,9]])
mat2=np.array([[3,2,1],[6,5,4],[9,8,7]])

print(mat1+mat2)

mat3=np.matmul(mat1,mat2)
print(mat3)