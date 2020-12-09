def part1(filename):
    with open(filename) as f:
        i = 0
        vals = []
        lines = list(map(int, f.read().splitlines()))
        while i < 25:
            vals.append(lines[i])
            i += 1
        for value in lines[25:]:
            total = list(map(lambda num: (value - num) not in vals, vals))
            if all(total):
                return (value)
            vals = vals[1:] + [value]
            # print(vals)


def part2(filename, invalid):
    with open(filename) as f:
        lines = list(map(int, f.read().splitlines()))
        vals = []
        idx = lines.index(invalid)
        for length in range (2, idx):
            chunks = [lines[i:i + length] for i in range(0, len(lines))]
            for chunk in chunks:
                if sum(chunk) == invalid:
                    return min(chunk) + max(chunk)

val = part1("input.txt")
print(val)
print(part2("input.txt", val))