def val(boarding_pass):
    return int(boarding_pass.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1'), 2)

def part1(filename):
    with open(filename) as f:
        ids = [val(line) for line in f.read().splitlines()]
        return max(ids)


def part2(filename):
    ids = []
    with open(filename) as f:
        ids = [val(line) for line in f.read().splitlines()]
    ids = sorted(ids)
    minimum, maximum = ids[0], ids[-1]
    ids = set(ids)
    all_ids = set(range(minimum, maximum))
    return (all_ids - ids).pop()



print(part1("input.txt"))
print(part2("input.txt"))