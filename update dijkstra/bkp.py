import random

def next_node(dist, q):
    min = 1e7
    min_index = None

    for node in q:
        if dist[node] < min:
            min = dist[node]
            min_index = node

    return min_index

def set_initial_conditions(maze, src):
    dist = {}
    prev = {}
    q = []

    for i in range(len(maze)):
        for j in range(len(maze[0])):
            dist[(i, j)] = 1e7
            prev[(i, j)] = None
            q.append((i, j))

    dist[src] = 0
    return dist, prev, q

def get_path(src, target, prev):
    s = []
    u = target
    while(u != src):
        s.append(u)
        u = prev[u]
    s.append(src)

    return s

def get_neighbors(node, size):
    neighbors = []
    if(node[1] + 1 < size): neighbors.append((node[0], node[1] + 1))
    if(node[0] + 1 < size): neighbors.append((node[0] + 1, node[1]))
    if(node[1] - 1 >= 0): neighbors.append((node[0], node[1] - 1))
    if(node[0] - 1 >= 0): neighbors.append((node[0] - 1, node[1]))

    return neighbors

def generate_maze(size):
    maze = [[random.randint(0, 1) for column in range(size)] for row in range(size)]
    return maze

def dijkstra_maze_solver(maze, src, target):
    dist, prev, not_visited = set_initial_conditions(maze, src)

    while(len(not_visited) > 0):
        node = next_node(dist, not_visited)
        if(node == target): break
        not_visited.pop(not_visited.index(node))

        neighbors = get_neighbors(node, len(maze))

        for n in neighbors:
            if (maze[n[0]][n[1]] > 0 and n in not_visited and dist[n] > dist[node] + 1):
                dist[n] = dist[node] + 1
                prev[n] = node

    return get_path(src, node, prev)

def draw_path(maze, path):
    clean_maze = list(map(lambda line: list(map(lambda element: " ", line)), maze))
    for i in path:
        clean_maze[i[0]][i[1]] = "*"

    return clean_maze

# maze = generate_maze(4)
maze = [[1, 0, 1, 1],
        [1, 1, 1, 0],
        [1, 1, 1, 0],
        [0, 0, 1, 1]]

for line in maze: print(line)
path = dijkstra_maze_solver(maze, (0, 0), (3, 3))
result = draw_path(maze, path)
for line in result: print(line)
