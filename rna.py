# Given an RNA sequence, such as ACAGU, we can predict its secondary structure 
#    by tagging each nucleotide as (, ., or ). Each matching pair of () must be 
#    AU, GC, or GU (or their mirror symmetries: UA, CG, UG). 
#    We also assume pairs can _not_ cross each other. 

from collections import defaultdict
from heapq import *

# Define the set of valid pairs for RNA sequences
pairs = set(['GU', 'UG', 'CG', 'GC', 'AU', 'UA'])

#    The following are valid structures for ACAGU:

#    ACAGU
#    .....
#    ...()
#    ..(.)
#    .(.).
#    (...)
#    ((.)) 

# We want to find the structure with the maximum number of matching pairs. 
#    In the above example, the last structure is optimal (2 pairs). 

#    best("ACAGU")
#    (2, '((.))')

#    Tie-breaking: arbitrary. Don't worry as long as your structure
#    is one of the correct best structures.

#    some other cases (more cases at the bottom):

#    GCACG
#    (2, '().()')
#    UUCAGGA
#    (3, '(((.)))')
#    GUUAGAGUCU
#    (4, '(.()((.)))')
#    AUAACCUUAUAGGGCUCUG
#    (8, '.(((..)()()((()))))')
#    AACCGCUGUGUCAAGCCCAUCCUGCCUUGUU
#    (11, '(((.(..(.((.)((...().))()))))))')
#    GAUGCCGUGUAGUCCAAAGACUUCACCGUUGG
#    (14, '.()()(()(()())(((.((.)(.))()))))')
#    CAUCGGGGUCUGAGAUGGCCAUGAAGGGCACGUACUGUUU
#    (18, '(()())(((((.)))()(((())(.(.().()()))))))')
#    ACGGCCAGUAAAGGUCAUAUACGCGGAAUGACAGGUCUAUCUAC
#    (19, '.()(((.)(..))(((.()()(())))(((.)((())))))())')
#    AGGCAUCAAACCCUGCAUGGGAGCACCGCCACUGGCGAUUUUGGUA
#    (20, '.(()())...((((()()))((()(.()(((.)))()())))))()')

# Function to find the structure with the maximum number of matching pairs
def best(sequence):
    
    # Function for dynamic programming to find the best score
    def _best(i, j):
        # Check if the score for this subsequence has already been calculated
        if (i, j) in OPT:
            return OPT[i, j]
        current = -1
        
        # Iterate through all possible splits of the sequence
        for k in range(i, j):
            # Check if splitting at position k improves the score
            if _best(i, k) + _best(k+1, j) > current:
                # Update the current best score
                current = max(current, _best(i, k) + _best(k+1, j))
                # Store the index of the split for backtracking
                back[i, j] = k
            
        # Check if adding a base pair at the ends improves the score
        if sequence[i] + sequence[j] in pairs:
            if _best(i+1, j-1) + 1 > current:
                current = _best(i+1, j-1) + 1
                back[i, j] =  -1
           
        # Store the best score for this subsequence
        OPT[i, j] = current
        return current
    
    # Function for backtracking to reconstruct the best structure
    def solution(i, j):
        if i == j: 
            return "."
        if i > j: 
            return ""
        k = back[i, j]
        if k == -1:
            return "(%s)" % solution(i+1, j-1)
        else:
            return solution(i, k) + solution(k+1, j)

    # Initialize dictionaries and variables
    OPT = defaultdict(int)
    back = {}
    seq_len = len(sequence)
    
    # Initialize base cases
    for i in range(seq_len):
        OPT[i, i] = 0
        OPT[i, i-1] = 0

    # Calculate the best score and the best structure
    return _best(0, seq_len-1), solution(0, seq_len-1)

# Total number of all possible structures

#    total("ACAGU")
#    6

# Function to calculate the total number of possible structures
def total(sequence):
    # Function for dynamic programming to count all possible structures
    def _total(i, j):
        if(i, j) in OPT:
            return OPT[i, j]

        countS = 0
        for k in range(i, j):
            if sequence[j] + sequence[k] in pairs:
                countS += _total(i, k-1) * _total(k+1, j-1)

        countS += _total(i, j-1)
        OPT[i, j] = countS

        return countS
        
    # Initialize dictionaries and variables
    OPT = defaultdict(int)
    seq_len = len(sequence)

    # Initialize base cases
    for i in range(seq_len):
        OPT[i, i] = 1
        OPT[i, i-1] = 1

    # Calculate the total number of possible structures
    return _total(0, seq_len-1)

# k-best structures: output the 1-best, 2nd-best, ... kth-best structures.

#    kbest("ACAGU", 3)
#    [(2, '((.))'), (1, '(...)'), (1, '.(.).')]
   
#    The list must be sorted. 
#    Tie-breaking: arbitrary.

#    In case the input k is bigger than the number of possible structures, output all.

#    Sanity check: kbest(s, 1)[0][0] == best(s)[0] for each RNA sequence s.

# Function to find the k-best structures
def kbest(sequence, k):
    # Function for dynamic programming to find the k-best structures
    def _kbest(i, j):
        # Helper function to try pushing a new structure to the heap
        def _trypushB(s, p, q):
            # Check if the indices are within bounds and the structure is not visited
            if p < len(bestk[i, s]) and q < len(bestk[s+1, j]) and (s, p, q) not in visited:
                # Push the score and indices to the heap
                heappush(h, (- (bestk[i, s][p][0] + bestk[s+1, j][q][0]), (s, p, q)))
                # Mark the structure as visited
                visited.add((s, p, q))

        def _trypushU(p):
            # Check if the index is within bounds and the structure is not visited
            if p < len(bestk[i+1, j-1]):
                # Push the score and index to the heap
                heappush(h, (- (bestk[i+1, j-1][p][0] + 1), (p,)))

        # Check if the k-best structures for this subsequence have already been calculated
        if (i, j) in bestk:
            return bestk[i, j]

        # Base cases
        if i == j:
            bestk[i, j] = [(0, '.')]
            return
        elif j == i - 1:
            bestk[i, i-1] = [(0, '')]
            return

        # Initialize a heap and a set to track visited structures
        h = []
        visited = set()

        # Iterate through all possible splits of the sequence
        for s in range(i, j):
            _kbest(i, s)
            _kbest(s+1, j)
            _trypushB(s, 0, 0)

        # Check if adding a base pair at the ends improves the score
        if sequence[i] + sequence[j] in pairs:
            _kbest(i+1, j-1)
            _trypushU(0)

        # Extract the k-best structures from the heap
        match = 0
        while match < k and h:
            _score, _indices = heappop(h)

            try:
                s, p, q = _indices
                result = (-_score, "%s%s" % (bestk[i, s][p][1], bestk[s+1, j][q][1]))

                # Add the new structure to the k-best list if it's not a duplicate
                if result not in bestk[i, j]:
                    bestk[i, j].append(result)
                    match += 1

                # Try pushing new structures based on the current one
                _trypushB(s, p+1, q)
                _trypushB(s, p, q+1)

            except:
                p = _indices[0]
                result = (-_score, "(%s)" % bestk[i+1, j-1][p][1])

                # Add the new structure to the k-best list if it's not a duplicate
                if result not in bestk[i, j]:
                    bestk[i, j].append(result)
                    match += 1

                # Try pushing new structures based on the current one
                _trypushU(p+1)

    # Initialize the dictionary to store k-best structures
    bestk = defaultdict(list)
    seq_len = len(sequence)
    _kbest(0, seq_len - 1)

    # return bestk[0, seq_len - 1] if k > len(bestk[0, seq_len - 1]) else bestk[0, seq_len - 1][:k]
    return _kbest(0, seq_len-1)
