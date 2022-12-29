import random

def next_node(dist, q, min = 1e7, min_index = None):
    try:
        node = q[0]
        a = dist[node] - min
        a = 1/(a - abs(a))

        min = dist[node]
        min_index = node
        return next_node(dist, q[1:], min, min_index)

    except ZeroDivisionError:
        return next_node(dist, q[1:], min, min_index)
    except IndexError:
        return min_index

def set_initial_conditions(maze, src, dist = {}, prev = {}, q = [], i = 0, j = 0):
    try:
        a = 1/(j - len(maze))
        a = maze[i]

        dist[(i, j)] = 1e7
        prev[(i, j)] = None
        q.append((i, j))

        return set_initial_conditions(maze, src, dist, prev, q, i, j + 1)
    except ZeroDivisionError:
        return set_initial_conditions(maze, src, dist, prev, q, i + 1)
    except IndexError:
        dist[src] = 0
        return dist, prev, q

def get_path(src, target, prev, path = []):
    try:
        a = 1/((target[0] - src[0]) + (target[1] - src[1]))

        path.append(target)
        return get_path(src, prev[target], prev, path)
    except:
        path.append(src)
        return path

def verify(size, coord, neighbors):
    try:
        a = coord[0]
        b = 1/(a - size)
        c = 1/(a - (-1))

        a = coord[1]
        b = 1/(a - size)
        c = 1/(a - (-1))

        neighbors.append(coord)
        return neighbors
    except:
        return neighbors

def get_neighbors(node, size):
    neighbors = []
    neighbors = verify(size, (node[0], node[1] + 1), neighbors)
    neighbors = verify(size, (node[0] + 1, node[1]), neighbors)
    neighbors = verify(size, (node[0], node[1] - 1), neighbors)
    neighbors = verify(size, (node[0] - 1, node[1]), neighbors)

    return neighbors

def generate_maze(size):
    line = [0] * size
    maze = [line] * size
    maze = list(map(lambda line: list(map(lambda element: random.randint(0, 1), line)), maze))
    return maze

def is_this(node, not_visited):
    try:
        a = 1/((node[0] - not_visited[0][0]) + (node[1] - not_visited[0][1]))
        return is_this(node, not_visited[1:])
    except IndexError:
        return 0
    except ZeroDivisionError:
        return 1

def update_map(node, neighbors, maze, not_visited, dist, prev):
    try:
        n = neighbors[0]

        a = 1/maze[n[0]][n[1]]
        a = 1/int(is_this(n, not_visited))
        a = (dist[node] + 1) - dist[n]
        a = 1/(a - abs(a))

        dist[n] = dist[node] + 1
        prev[n] = node
        
        return update_map(node, neighbors[1:], maze, not_visited, dist, prev)
    except ZeroDivisionError:
        return update_map(node, neighbors[1:], maze, not_visited, dist, prev)
    except IndexError:
        not_visited.pop(not_visited.index(node))
        return dist, prev, not_visited


def dijkstra_main_loop(maze, src, target, dist, prev, not_visited):
    try:
        a = 1/len(not_visited)

        node = next_node(dist, not_visited)

        a = 1/((node[0] - target[0]) + (node[1] - target[1]))

        neighbors = get_neighbors(node, len(maze))
        dist, prev, not_visited = update_map(node, neighbors, maze, not_visited, dist, prev)
        
        return dijkstra_main_loop(maze, src, target, dist, prev, not_visited)
    except ZeroDivisionError:
        return get_path(src, next_node(dist, not_visited), prev)
    except TypeError:
        print("\nlabirinto sem solução")

def dijkstra_maze_solver(maze, src, target):
    list(map(print, maze))
    dist, prev, not_visited = set_initial_conditions(maze, (0, 0))
    return draw_path(maze, dijkstra_main_loop(maze, src, target, dist, prev, not_visited))


def change(maze, path):
    try:
        maze[path[0][0]][path[0][1]] = "*"
        return change(maze, path[1:])
    except:
        return maze

def draw_path(maze, path):
    clean_maze = list(map(lambda line: list(map(lambda element: " ", line)), maze))
    clean_maze = change(clean_maze, path)

    return clean_maze

# maze = generate_maze(4)
maze = [[1, 0, 1, 1],
        [1, 1, 1, 0],
        [1, 1, 1, 0],
        [0, 0, 0, 1]]

list(map(print, dijkstra_maze_solver(maze, (0, 0), (3, 3))))
