def part1(filename):
    with open(filename) as f:
        adaptors = list(map(int, f.readlines()))
        adaptors = sorted(adaptors)
        prev = 0
        one = 0
        three = 0
        for adaptor in adaptors:
            diff = adaptor - prev
            prev = adaptor
            if diff == 1:
                one += 1
            elif diff == 3:
                three += 1
        return one * (three + 1)

def part2(filename):
    with open(filename) as f:
        adaptors = sorted(list(map(int, f.readlines())))
        val = max(adaptors)
        return find_arrangements(adaptors, val)


results = {}
def find_arrangements(adaptors, number):
    if number == 0:
        return 1
    if len(adaptors) == 0:
        return 0
    if (number, adaptors[-1]) in results:
        return results[(number, adaptors[-1])]
    if adaptors[-1] == number:
        ans = find_arrangements(adaptors[:-1], number-1) + find_arrangements(adaptors[:-1], number-2) + find_arrangements(adaptors[:-1], number-3)
        results[(number, adaptors[-1])] = ans
        return ans
    else:
        ans =  find_arrangements(adaptors[:-1], number)
        results[(number, adaptors[-1])] = ans
        return ans

print(part1("input.txt"))
print(part2("input.txt"))