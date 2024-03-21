from collections import defaultdict
from heapq import *

pairs = set(['GU', 'UG', 'CG', 'GC', 'AU', 'UA'])

def best(sequence):
    
    def _best(i, j):
        if (i, j) in OPT:
            return OPT[i, j]
        current = -1
        for k in range(i, j):
            if _best(i, k) + _best(k+1, j) > current:
                current = max(current, _best(i, k) + _best(k+1, j))
                back[i, j] = k
            
        if sequence[i] + sequence[j] in pairs:
            if _best(i+1, j-1) + 1 > current:
                current = _best(i+1, j-1) + 1
                back[i, j] =  -1
           
        OPT[i, j] = current
        return current
    

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

    OPT = defaultdict(int)
    back = {}
    seq_len = len(sequence)
    for i in range(seq_len):
        OPT[i, i] = 0
        OPT[i, i-1] = 0

    return _best(0, seq_len-1), solution(0, seq_len-1)



def total(sequence):
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
        
    OPT = defaultdict(int)
    seq_len = len(sequence)

    for i in range(seq_len):
        OPT[i, i] = 1
        OPT[i, i-1] = 1

    return _total(0, seq_len-1)



def kbest(sequence, k):
    def _kbest(i, j):
        def _trypushB(s, p, q):
            if p < len(bestk[i, s]) and q < len(bestk[s+1, j]) and (s, p, q) not in visited:
                heappush(h,(- (bestk[i, s][p][0] + bestk[s+1, j][q][0]),(s, p, q)))
                visited.add((s, p, q))

        def _trypushU(p):
            if p < len(bestk[i+1,j-1]):
                heappush(h, (- (bestk[i+1, j-1][p][0]+1),(p,)))

        if (i, j) in bestk:
            return bestk[i, j]

        if i==j:
            bestk[i, j] = [(0,'.')]
            return
        
        elif j == i-1:
            bestk[i, i-1] = [(0, '')]
            return

        h = []
        visited = set()
        
        for s in range(i, j):
            _kbest(i, s)
            _kbest(s+1, j)
            _trypushB(s, 0, 0)

        if sequence[i]+sequence[j] in pairs:
            _kbest(i+1, j-1)
            _trypushU(0)

        match = 0
        while match < k:
            if h == []:
                break
            
            _score, _indices = heappop(h)
            
            try:
                s,p,q = _indices
                result = (-_score, "%s%s" % (bestk[i,s][p][1],bestk[s+1,j][q][1]))

                if result not in bestk[i, j]:
                    bestk[i, j].append(result)
                    match += 1
                    

                _trypushB(s, p+1, q)
                _trypushB(s, p, q+1)
                
            except:
                p = _indices[0]
                result = (-_score, "(%s)" % bestk[i+1, j-1][p][1])
               

                if result not in bestk[i, j]:
                    bestk[i, j].append(result)
                    match += 1
                    

                _trypushU(p+1)

    bestk = defaultdict(list)
    seq_len = len(sequence)
    _kbest(0, seq_len-1)
  
    return _kbest(0, seq_len-1)

# print(kbest("ACAGU",10))