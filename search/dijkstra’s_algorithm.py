from queue import deque


def dijkstra(start, graph):
    min_dist = {}
    min_dist[start] = 0
    queue = deque(start)
    while queue:
        curr = queue.popleft()
        for vertex in graph[curr]:
            if vertex not in min_dist or min_dist[curr] + graph[curr][vertex] < min_dist[vertex]:
                min_dist[vertex] = min_dist[curr] + graph[curr][vertex]
                queue.append(vertex)
    print(min_dist)


graph = {'A': {'B': 2, 'H': 15},
         'B': {'C': 1, 'D': 5},
         'C': {'B': 1, 'D': 3, 'G': 1, 'F': 2},
         'D': {'B': 5, 'C': 3, 'F': 4, 'E': 6},
         'E': {'D': 6, 'F': 7, 'I': 2},
         'F': {'C': 2, 'D': 4, 'G': 1, 'E': 7, 'H': 3},
         'G': {'C': 1, 'F': 1},
         'H': {'A': 15, 'F': 3, 'I': 12},
         'I': {'H': 12, 'E': 2}
         }

dijkstra('A', graph)
