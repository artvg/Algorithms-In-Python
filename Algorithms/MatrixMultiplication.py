# Matrix Multiplication using Divide and Conquer

# PART 1
def iterative_matrix_multiply(A, B):
    n = len(A)
    # Initialize C as an n x n zero matrix
    C = [[0 for _ in range(n)] for _ in range(n)]

    # Triple nested loop to perform matrix multiplication
    for i in range(n):  # row of A
        for j in range(n):  # column of B
            for k in range(n):  # shared dimension
                C[i][j] += A[i][k] * B[k][j]  # multiply and accumulate
    return C

# Test Case for Part 1
A1 = [[1, 2], [2, 3]]
B1 = [[4, 5], [6, 7]]

result1 = iterative_matrix_multiply(A1, B1)
print("Iterative Multiplication Result:")
for row in result1:
    print(row)


# PART 2
def add_matrix(X, Y):
    # Addition of two matrices
    n = len(X)
    return [[X[i][j] + Y[i][j] for j in range(n)] for i in range(n)]

def split_matrix(M):
    # Splits a matrix into 4 equal submatrices
    n = len(M)
    mid = n // 2
    A11 = [row[:mid] for row in M[:mid]]
    A12 = [row[mid:] for row in M[:mid]]
    A21 = [row[:mid] for row in M[mid:]]
    A22 = [row[mid:] for row in M[mid:]]
    return A11, A12, A21, A22

def join_matrices(C11, C12, C21, C22):
    # Joins 4 submatrices into one
    top = [c11 + c12 for c11, c12 in zip(C11, C12)]
    bottom = [c21 + c22 for c21, c22 in zip(C21, C22)]
    return top + bottom

def recursive_matrix_multiply(A, B):
    n = len(A)

    # Single element multiplication
    if n == 1:
        return [[A[0][0] * B[0][0]]]

    # Divide A and B into 4 submatrices each
    A11, A12, A21, A22 = split_matrix(A)
    B11, B12, B21, B22 = split_matrix(B)

    # Recursively compute submatrices of C based on formula
    C11 = add_matrix(recursive_matrix_multiply(A11, B11), recursive_matrix_multiply(A12, B21))
    C12 = add_matrix(recursive_matrix_multiply(A11, B12), recursive_matrix_multiply(A12, B22))
    C21 = add_matrix(recursive_matrix_multiply(A21, B11), recursive_matrix_multiply(A22, B21))
    C22 = add_matrix(recursive_matrix_multiply(A21, B12), recursive_matrix_multiply(A22, B22))

    # Combine submatrices into final result matrix
    return join_matrices(C11, C12, C21, C22)

# Test Case for Part 2
A2 = [[1, 2, 3, 4],
      [5, 6, 7, 8],
      [9, 10, 11, 12],
      [13, 14, 15, 16]]

B2 = [[1, 2, 3, 4],
      [5, 6, 7, 8],
      [9, 10, 11, 12],
      [13, 14, 15, 16]]

result2 = recursive_matrix_multiply(A2, B2)
print("\nRecursive Multiplication Result:")
for row in result2:
    print(row)
