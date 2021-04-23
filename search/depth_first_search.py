def dfs(vertex, graph, used):
    used.add(vertex)
    for neighbour in graph[vertex]:
        if neighbour not in used:
            dfs(neighbour, graph, used)


graph = {'A': {'C'},
         'B': {'C'},
         'C': {'A', 'B', 'D'},
         'D': {'E', 'G', 'H'},
         'E': {'D', 'F'},
         'F': {'E'},
         'G': {'D'},
         'H': {'D', 'K'},
         'K': {'H'},
         'I': set()
         }
used = set()
component = 0

for vertex in graph:
    if vertex not in used:
        dfs(vertex, graph, used)
        component += 1

print(component)
