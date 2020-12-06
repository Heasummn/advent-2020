def count_trees(tree, slope):
    cnt = 0
    row, col = slope
    while row < len(tree):
        if tree[row][col]:
            cnt += 1
        col = (col + slope[1]) % len(tree[0])
        row += slope[0]

    return cnt

def part1(filename):
    tree = []
    with open(filename) as f:
        for line in f.read().splitlines():
            tree.append(list(map(lambda x: x == "#", line)))
            #tree.append(list(line))
    return count_trees(tree, (1, 3))

def part2(filename):
    tree = []
    with open(filename) as f:
        for line in f.read().splitlines():
            tree.append(list(map(lambda x: x == "#", line)))
            #tree.append(list(line))
    slopes = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
    product = 1
    for slope in slopes:
        product *= count_trees(tree, slope)

    return product



print(part1("input.txt"))
print(part2("input.txt"))