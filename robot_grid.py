def can_move(grid, pos):
    if not pos:
        return False
    x, y = pos
    if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
        return True
    return False

def robot_grid(grid, cur, end, path):
    if not cur or not can_move(grid, cur):
        return None
    path.append(cur)
    if cur == end:
        return path
    x, y = cur
    d_path = robot_grid(grid, (x+1, y), end, path)
    r_path = robot_grid(grid, (x, y+1), end, path)
    if d_path:
        return d_path
    if r_path:
        return r_path


def main():
    grid = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]
    start = (0, 0)
    end = (2, 2)
    path = list()
    print(robot_grid(grid, start, end, path))

if __name__ == "__main__":
    main()
