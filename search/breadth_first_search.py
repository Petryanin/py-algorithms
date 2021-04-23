from queue import deque
from collections import namedtuple

# Knight paths
numbers = '12345678'
letters = 'abcdefgh'


def bfs(start, end, graph):
    queue = deque([start])
    min_distance = {i: None for i in graph}
    parent = {i: None for i in graph}
    min_distance[start] = 0
    while queue:
        curr = queue.popleft()
        for vertex in graph[curr]:
            if min_distance[vertex] is None:
                min_distance[vertex] = min_distance[curr] + 1
                parent[vertex] = curr
                queue.append(vertex)
    return parent, min_distance[end]


def get_chessboard():
    chessboard = dict()
    for i in letters:
        for j in numbers:
            chessboard[i + j] = set()
    return chessboard


def add_edge(graph, v1, v2):
    graph[v1].add(v2)
    graph[v2].add(v1)


def init_knight_paths(graph):
    for i in range(8):
        for j in range(8):
            v1 = letters[i] + numbers[j]
            if 0 <= i + 2 < 8 and 0 <= j + 1 < 8:
                v2 = letters[i + 2] + numbers[j + 1]
                add_edge(graph, v1, v2)
            if 0 <= i + 1 < 8 and 0 <= j + 2 < 8:
                v2 = letters[i + 1] + numbers[j + 2]
                add_edge(graph, v1, v2)
            if 0 <= i - 1 < 8 and 0 <= j + 2 < 8:
                v2 = letters[i - 1] + numbers[j + 2]
                add_edge(graph, v1, v2)
            if 0 <= i - 2 < 8 and 0 <= j + 1 < 8:
                v2 = letters[i - 2] + numbers[j + 1]
                add_edge(graph, v1, v2)


graph = get_chessboard()
init_knight_paths(graph)
BFS = namedtuple('BFS', 'parent min_distance')


start, end = input('Input start and end positions: ').split()
res = BFS(*bfs(start, end, graph))

path = []
path.append(end)

while path[-1] != start:
    parent = res.parent[path[-1]]
    path.append(parent)

path = path[::-1]
path.remove(end)


print('Minimal distance: ', res.min_distance)
print('Path:')
for vertex in path:
    print(vertex, end=' -> ')
print(end)
