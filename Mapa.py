def try_coloring():

    graph = {
        'A': ['B', 'E', 'F'],
        'B': ['A', 'E','F','G','C'],
        'C': ['B', 'G', 'H', 'D'],
        'D': ['C','H'],
        'E': ['A', 'B','F','H'],
        'F': ['B', 'G','E','H'],
        'G': ['B', 'C','F','H'],
        }
    num_colors = 3
    assert num_colors >= 0, "Invalid number of colors: %s" % num_colors
    colors = {}
 
    def neighbors_have_different_colors(nodes, color):
        return all(color != colors.get(n) for n in nodes)
 
    for node, adjacents in graph.items():
 
        found_color = False
 
        for color in range(num_colors):
            if neighbors_have_different_colors(adjacents, color):
                found_color = True
                colors[node] = color
                break
 
        if not found_color:
            return None
 
    return colors
 
 
def find_graph_colors(graph):
    for num_colors in range(1, len(graph)):
        colors = try_coloring(graph, num_colors)
        if colors:
            return colors

grafo = try_coloring()
print(grafo)
