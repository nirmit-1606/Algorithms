# Number of n-node BSTs

#    input: n
#    output: number of n-node BSTs

#    bsts(2)    returns 2
#    bsts(3)    returns 5
#    bsts(5)    returns 42

#    [HINT] There are two 2-node BSTs:
#       2    1
#      /      \
#     1        2
#    Note that all other 2-node BSTs are *isomorphic* to either one.

def bsts(n):
    res = 1  # Initialize the result to 1

    # Iterate from 0 to n-1
    for i in range(n):
        # Update the result by multiplying it with (2n - i)
        res *= (2*n - i)
        # Update the result by dividing it by (i + 1)
        res //= (i + 1)

    # Divide the result by (n + 1) to obtain the final count of n-node BSTs
    return res // (n + 1)
