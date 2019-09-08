# Algoritmo de Caminho Mínimo

def CM( atual, pai, dist, destino ):
    if ( atual == destino ):
        print (dist)
        return True

    for [c,d] in g[atual]:
        if ( c != pai ):
            if ( CM( c, atual, dist + d, destino ) ):
                return True

    return False
            
[N, A, B] = [int(c) for c in input().split()]

g = [[] for i in range(N+1)]

for i in range(1,N):
    [P, Q, D] = [int(c) for c in input().split()]
    g[P].append( [Q, D] )
    g[Q].append( [P, D] )

CM( A, -1, 0, B )