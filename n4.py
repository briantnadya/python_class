def permutation(n, k):
    result = n
    for i in range(1, k):
        result = result * (n - i)
    return result


# we can calculate the permutations for any n and k
print(permutation(10, 5))
