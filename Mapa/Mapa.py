cores = {}

def vizinho(nos, cor):
    return all(cor != cores.get(n) for n in nos)

def colorir():

    grafo = {
        'A': ['B', 'E', 'F'],
        'E': ['A', 'B','F','H'],
        'B': ['A', 'E','F','G','C'],
        'C': ['B', 'G', 'H', 'D'],
        'D': ['C','H'],
        'F': ['B', 'G','E','H'],
        'G': ['B', 'C','F','H'],
        'H': ['E','F','G','C','D']
        }
    num_cores = 3
        
    for no, adjacentes in grafo.items():
 
        cor_encontrada = False
 
        for cor in range(num_cores):
            if vizinho(adjacentes, cor):
                cor_encontrada = True
                cores[no] = cor
                break
 
        if not cor_encontrada:
            return None
 
    return cores

grafo = colorir()
print(grafo)
