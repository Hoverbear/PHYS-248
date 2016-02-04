import sympy
import copy

def swap(matrix, vector, index_a, index_b):
   # Matrix
   source = matrix[index_a]
   matrix[index_a] = matrix[index_b]
   matrix[index_b] = source
   # Vector
   source = vector[index_a]
   vector[index_a] = vector[index_b]
   vector[index_b] = source

def divide(matrix, vector, index, divisor):
    for i in range(0, len(matrix[index])):
        matrix[index][i] /= divisor
    vector[index] /= divisor

def argmax(ingress, function):
    max_value = 0
    max_index = 0
    for i in ingress:
        if function(i) > max_value:
            max_value = function(i)
            max_index = i
    return max_index


def gaussian_elimination(A_matrix, u_vector):
    A_matrix = copy.deepcopy(A_matrix)
    u_vector = copy.deepcopy(u_vector)
    # Make sure this matrix doesn't suck.
    if len(A_matrix) == 0:
        raise ValueError("Empty matrix.")
    m_length = len(A_matrix[0])
    for i in range(1, len(A_matrix)):
        if len(A_matrix[i]) != m_length:
            raise ValueError("Matrix rows not same length")
    n_length = len(A_matrix[0])

    # Start algorithm.
    for k in range(0, min(n_length, m_length)):
        # Find the k-th pivot.
        i_max = argmax(range(k, m_length), lambda x: abs(A_matrix[x][k]))
        if A_matrix[i_max][k] == 0:
            raise ValueError("Matrix is singular")
        swap(A_matrix, u_vector, k, i_max)
        # Do for all rows below pivot.
        for i in range(k+1, m_length):
            #print("k:", k, ", i:", i, ", A_matrix[k][k]:", A_matrix[k][k])
            m = A_matrix[i][k] / A_matrix[k][k]
            # Do for all elements of the current row.
            for j in range(k+1, n_length):
                A_matrix[i][j] -= A_matrix[k][j] * m
            u_vector[i] -= u_vector[k] * m
            # Fill the lower with 0s
            A_matrix[i][k] = 0

    # print("Minimizes to:", A_matrix, u_vector)

    # Back subtitute.
    for i in range(len(A_matrix)-1, -1, -1):
        u_vector[i] /= A_matrix[i][i]
        A_matrix[i][i] = 1
        for j in range(len(A_matrix)-1, -1, -1):
            # Remove all terms of this column
            A_matrix[j][i] -= A_matrix[i][i] * A_matrix[j][i]
            u_vector[j] -= u_vector[i] * A_matrix[j][i]

    return u_vector
