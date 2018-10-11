def can_move(grid, pos):
    r, c = pos
    if 0 <= r < len(grid) \
      and 0 <= c < len(grid[0]) \
      and grid[r][c]:
        return True
    else:
        return False

def robot_grid(grid, curr, end, curr_path, paths):
    r, c = curr
    new_path = curr_path + [curr]
    if curr == end:
        paths.append(new_path)
        return None
    else:
        right = (r,c+1)
        if can_move(grid, right):
            robot_grid(grid, right, end, new_path, paths)
        down = (r+1,c)
        if can_move(grid, down):
            robot_grid(grid, down, end, new_path, paths)
        return None


def main():
    grid = [[1, 1, 1],
            [1, 1, 1],
            [1, 1, 1]]
    start = (0, 0)
    end = (2, 2)
    curr_path = list()
    paths = list()
    robot_grid(grid, start, end, curr_path, paths)
    print(paths)

if __name__ == "__main__":
    main()
