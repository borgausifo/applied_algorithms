def mysteryfunction(A, right):
    if right == 0:
        return A[0]
    else:
        val = mysteryfunction(A, right - 1)
        if A[right] > val:
            val = A[right]
        return val

A = [1, 3, 4, 6, 7, 2]

print(mysteryfunction(A, 5))

B = [34, 54, 2, 12, 45, 89, 88, 67, 1]

print(mysteryfunction(B, 8))

