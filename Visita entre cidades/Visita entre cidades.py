def BEP(atual,pai,destino,distancia):
    if atual==destino:
        print(distancia)
    for [i,j] in A[atual]:
        if ( i != pai ):
          BEP(i,atual,destino,distancia+j)

[n,origem,destino]=[int(x)for x in input().split()]
A= [[] for i in range(n+1)]

for i in range(1,n):
    [P, Q, D] = [int(c) for c in input().split()]
    A[P].append( [Q, D] )
    A[Q].append( [P, D] )

BEP(origem,None,destino,0)
