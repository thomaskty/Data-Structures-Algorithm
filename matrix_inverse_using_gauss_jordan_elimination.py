def inverse_matrix(matrix):
    # Check if the matrix is square
    if len(matrix) != len(matrix[0]):
        raise ValueError("Input matrix must be square for inversion")

    n = len(matrix)
    
    # Create an augmented matrix [matrix | identity]
    augmented_matrix = [row + [1 if i == j else 0 for j in range(n)] for i, row in enumerate(matrix)]

    # Perform Gauss-Jordan elimination
    for i in range(n):
        # Normalize the current row
        pivot = augmented_matrix[i][i]
        for j in range(2 * n):
            augmented_matrix[i][j] /= pivot
        
        # Eliminate other rows
        for k in range(n):
            if k != i:
                factor = augmented_matrix[k][i]
                for j in range(2 * n):
                    augmented_matrix[k][j] -= factor * augmented_matrix[i][j]

    # Extract the inverse matrix from the augmented matrix
    inverse = [row[n:] for row in augmented_matrix]

    return inverse

# Example usage
matrix = [
    [4, 7],
    [2, 6]
]

inverse_matrix_result = inverse_matrix(matrix)
for row in inverse_matrix_result:
    print(row)

