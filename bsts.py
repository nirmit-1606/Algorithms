def bsts(n):
    res = 1

    for i in range(n):
        res *= (2*n - i)
        res //= (i + 1)

    return res // (n + 1)

print(bsts(2))

print(bsts(3))

print(bsts(5))