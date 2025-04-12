import numpy as np


vector_10_49 = np.arange(10, 50)


matrix_0_8 = np.arange(9).reshape(3, 3)


identity_3x3 = np.eye(3)


array_3x3x3 = np.random.rand(3, 3, 3)


array_10x10 = np.random.rand(10, 10)
min_val = array_10x10.min()
max_val = array_10x10.max()


random_vector_30 = np.random.rand(30)
mean_val = random_vector_30.mean()


matrix_5x5 = np.random.rand(5, 5)
normalized_5x5 = (matrix_5x5 - matrix_5x5.min()) / (matrix_5x5.max() - matrix_5x5.min())


matrix_5x3 = np.random.rand(5, 3)
matrix_3x2 = np.random.rand(3, 2)
product_5x2 = np.dot(matrix_5x3, matrix_3x2)

mat1_3x3 = np.random.rand(3, 3)
mat2_3x3 = np.random.rand(3, 3)
dot_product_3x3 = np.dot(mat1_3x3, mat2_3x3)

matrix_4x4 = np.random.rand(4, 4)
transpose_4x4 = matrix_4x4.T


matrix_det_3x3 = np.random.rand(3, 3)
determinant = np.linalg.det(matrix_det_3x3)


A_3x4 = np.random.rand(3, 4)
B_4x3 = np.random.rand(4, 3)
product_AB = np.dot(A_3x4, B_4x3)


matrix_3x3 = np.random.rand(3, 3)
vector_3x1 = np.random.rand(3, 1)
matrix_vector_product = np.dot(matrix_3x3, vector_3x1)


A = np.random.rand(3, 3)
b = np.random.rand(3)
x = np.linalg.solve(A, b)

matrix_5x5_sum = np.random.rand(5, 5)
row_sums = matrix_5x5_sum.sum(axis=1)
col_sums = matrix_5x5_sum.sum(axis=0)
