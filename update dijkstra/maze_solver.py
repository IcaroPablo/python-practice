import random

D, L, R = 'data', 'left', 'right'

def insert(tree, data):
    if tree is None:
        tree = {D: data, L: None, R: None}
    elif data <= tree[D]:
        tree[L] = insert(tree[L], data)
    else:
        tree[R] = insert(tree[R], data)
    return tree


def traverse(tree):
    if tree is not None:
        for data in traverse(tree[L]):
            yield data
        yield tree[D]
        for data in traverse(tree[R]):
            yield data

def generate_maze(size):
    maze = [[]]
    for i in range(size):
        line = []
        for j inrange(size):
            line.append(random.randint(0,1))
        maze.append(line)

    print(maze)
    return maze

def pos_v(maze, point):
    return maze[point[0]][point[1]]

a = list(range(32))
shuffle(a)
print(*a)

tree = None
for i in a:
    tree = insert(tree, i)

print(*traverse(tree))

def pos_s(a, direction):
    if(direction == "u")
        return [a[0], a[1] + 1]
    if(direction == "r")
        return [a[0] + 1, a[1]]
    if(direction == "d")
        return [a[0], a[1] - 1]
    if(direction == "l")
        return [a[0] - 1, a[1]]

def generate_maze_map(maze, a):
    

def find_path(maze, a, b):
    p1 = pos_v(maze, pos_s(a, "u"))
    if(p1 == 1):
        increment_path(p1)
    p2 = pos_v(maze, pos_s(a, "u"))
    if(p1 == 1):
        increment_path(p1)
    p1 = pos_v(maze, pos_s(a, "u"))
    if(p1 == 1):
        increment_path(p1)

