def min_moves_to_sort(A):
    LIS_length = 1
    for i in range(1, len(A)):
        if A[i] > A[i - 1]:
            LIS_length += 1

    # Minimum number of moves = Total elements - Length of LIS
    return len(A) - LIS_length

# Example usage
A = [5, 2, 6, 1, 3, 7, 4]
print("Minimum number of moves required:", min_moves_to_sort(A))
