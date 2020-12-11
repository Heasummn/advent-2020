def new_value(col, row, grid):
    indices = []
    if col != 0:
        indices.append((col - 1, row))
        if row != 0:
            indices.append((col - 1, row - 1))
        if row != len(grid) - 1:
            indices.append((col - 1, row + 1))
    if col != len(grid[0]) - 1:
        indices.append((col + 1, row))
        if row != 0:
            indices.append((col + 1, row - 1))
        if row != len(grid) - 1:
            indices.append((col + 1, row + 1))
    if row != 0:
        indices.append((col, row - 1))
    if row != len(grid) - 1:
        indices.append((col, row + 1))
    if grid[row][col] == 'L':
        condition = lambda index: grid[index[1]][index[0]] == 'L' or grid[index[1]][index[0]] == '.'
        if all(map(condition, indices)):
            return True
    elif grid[row][col] == '#':
        condition = lambda index: grid[index[1]][index[0]] == '#'
        if sum(map(condition, indices)) >= 4:
            return True
    return False


def step(grid):
    to_flip = []
    for row_idx, row in enumerate(grid):
        for col_idx in range(len(row)):
            if new_value(col_idx, row_idx, grid):
                to_flip.append((row_idx, col_idx))
    for row, col in to_flip:
        if grid[row][col] == 'L':
            grid[row][col] = '#'
        elif grid[row][col] == '#':
            grid[row][col] = 'L'
    return len(to_flip), grid

def part1(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
        grid = list(map(list, lines))
        flipped = -1
        while flipped != 0:
            flipped, grid = step(grid)

        busy_cnt = 0
        for row in grid:
            for col in row:
                busy_cnt += (col == '#')
        return busy_cnt


def new_value_part2(col, row, grid):
    visible_col = col - 1
    visible_row = row
    indices = []
    # left and right
    while visible_col >= 0:
        if grid[visible_row][visible_col] in ['#', 'L']:
            indices.append((visible_col, visible_row))
            break
        visible_col -= 1
    visible_col = col + 1
    while visible_col < len(grid[0]):
        if grid[visible_row][visible_col] in ['#', 'L']:
            indices.append((visible_col, visible_row))
            break
        visible_col += 1
    visible_col = col

    # up and down
    visible_row = row - 1
    while visible_row >= 0:
        if grid[visible_row][visible_col] in ['#', 'L']:
            indices.append((visible_col, visible_row))
            break
        visible_row -= 1
    visible_row = row + 1
    while visible_row < len(grid):
        if grid[visible_row][visible_col] in ['#', 'L']:
            indices.append((visible_col, visible_row))
            break
        visible_row += 1

    visible_col = col - 1
    visible_row = row - 1
    # both neg
    while visible_row >= 0 and visible_col >= 0:
        if grid[visible_row][visible_col] in ['#', 'L']:
            indices.append((visible_col, visible_row))
            break
        visible_row -= 1
        visible_col -= 1

    visible_col = col + 1
    visible_row = row - 1
    # col increasing, row decreasing
    while visible_row >= 0 and visible_col < len(grid[0]):
        if grid[visible_row][visible_col] in ['#', 'L']:
            indices.append((visible_col, visible_row))
            break
        visible_row -= 1
        visible_col += 1

    visible_row = row + 1
    visible_col = col - 1
    # row increasing, col decreasing
    while visible_row < len(grid) and visible_col >= 0:
        if grid[visible_row][visible_col] in ['#', 'L']:
            indices.append((visible_col, visible_row))
            break
        visible_row += 1
        visible_col -= 1

    visible_row = row + 1
    visible_col = col + 1
    # both positive
    while visible_row < len(grid) and visible_col < len(grid[0]):
        if grid[visible_row][visible_col] in ['#', 'L']:
            indices.append((visible_col, visible_row))
            break
        visible_row += 1
        visible_col += 1

    if grid[row][col] == 'L':
        condition = lambda index: grid[index[1]][index[0]] == 'L' or grid[index[1]][index[0]] == '.'
        if all(map(condition, indices)):
            return True
    elif grid[row][col] == '#':
        condition = lambda index: grid[index[1]][index[0]] == '#'
        if sum(map(condition, indices)) >= 5:
            return True
    return False

def step_part2(grid):
    to_flip = []
    for row_idx, row in enumerate(grid):
        for col_idx in range(len(row)):
            if new_value_part2(col_idx, row_idx, grid):
                to_flip.append((row_idx, col_idx))
    for row, col in to_flip:
        if grid[row][col] == 'L':
            grid[row][col] = '#'
        elif grid[row][col] == '#':
            grid[row][col] = 'L'
    return len(to_flip), grid


def part2(filename):
   with open(filename) as f:
        lines = f.read().splitlines()
        grid = list(map(list, lines))

        cnt = -1

        while cnt != 0:
            cnt, grid = step_part2(grid)

        busy_cnt = 0
        for row in grid:
            for col in row:
                busy_cnt += (col == '#')
        return busy_cnt



print(part1("input.txt"))
print(part2("input.txt"))