# Number of bit strings of length n that has

#    1) no two consecutive 0s.
#    2) two consecutive 0s.
   
#    num_no(3)      returns 5
#    num_yes(3)     returns 3

#    [HINT] There are three 3-bit 0/1-strings that have two consecutive 0s.
#               001  100  000
#           The other five 3-bit 0/1-strings have no two consecutive 0s:
# 	            010  011  101  110  111

def num_no(n):
    # Initialize arrays to store counts
    a = [0 for i in range(n)]
    b = [0 for i in range(n)]
    
    # Initialize the first elements of arrays a and b to 1
    a[0] = b[0] = 1
    
    # Iterate from the second element to the last
    for i in range(1, n):
        # Calculate the count of bit strings with no consecutive zeros
        a[i] = a[i - 1] + b[i - 1]
        # Calculate the count of bit strings ending with zero
        b[i] = a[i - 1]
     
    # Return the total count of bit strings with no consecutive zeros
    return a[n - 1] + b[n - 1]

def num_yes(n):
    # The total number of bit strings of length n is 2^n
    # Subtract the count of bit strings with no consecutive zeros from 2^n to get the count of bit strings with consecutive zeros
    return 2 ** n - num_no(n)
