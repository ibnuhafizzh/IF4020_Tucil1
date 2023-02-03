import numpy as np

def adjoint(A):
    # Check if matrix is square
    rows, cols = np.shape(A)
    if rows != cols:
        raise ValueError("Matrix is not square")

    # Find the adjoint matrix
    adjA = np.zeros((rows, cols))
    for i in range(rows):
        for j in range(cols):
            adjA[i][j] = (-1)**(i+j) * np.linalg.det(np.delete(np.delete(A, i, axis=0), j, axis=1))
    return np.transpose(adjA)

def det(matrix):
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    elif n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        determinant = 0
        for i in range(n):
            sub_matrix = [[matrix[j][k] for k in range(n) if k != i] for j in range(1, n)]
            determinant += (-1)**i * matrix[0][i] * det(sub_matrix)
        return determinant

def determinant_mod(matrix):
    determinant = det(matrix)
    print(determinant)
    determinant = determinant%26
    print(determinant)
    return determinant
def inverse_modulo(a, m):
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def modulo_inverse_mat(matrix, mod):
    adjoin_mat = adjoint(matrix)
    det_mod = determinant_mod(matrix)
    inverse_mod = inverse_modulo(det_mod,26)
    adjoin_mat = adjoin_mat*inverse_mod

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            adjoin_mat[i][j] = adjoin_mat[i][j]%mod
    return adjoin_mat

# Example usage
A = [[7,11,0], [4,14,15],[11,2,19]]
print(modulo_inverse_mat(A, 26))
