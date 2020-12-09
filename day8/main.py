from copy import deepcopy

def part1(filename):
    with open(filename) as f:
        parsed = []
        for line in f:
            tokens = line.split()
            parsed.append({"op": tokens[0], "val": int(tokens[1])})
        visited = set()
        isp = 0
        acc = 0
        while True:
            if isp in visited:
                break
            visited.add(isp)
            op = parsed[isp]["op"]
            if op == "nop":
                isp += 1
                continue
            if op == "acc":
                acc += parsed[isp]["val"]
                isp += 1
                continue
            if op == "jmp":
                isp += parsed[isp]["val"]
        return acc

def does_loop(program):
    isp = 0
    acc = 0
    visited = set()
    while isp < len(program):
        if isp in visited:
            return (True, -1)
        visited.add(isp)
        op = program[isp]["op"]
        if op == "nop":
            isp += 1
            continue
        if op == "acc":
            acc += program[isp]["val"]
            isp += 1
            continue
        if op == "jmp":
            isp += program[isp]["val"]
    return (False, acc)

def part2(filename):
    with open(filename) as f:
        parsed = []
        for line in f:
            tokens = line.split()
            parsed.append({"op": tokens[0], "val": int(tokens[1])})
        loops, acc = does_loop(parsed)
        isp = 0
        while loops:
            program = deepcopy(parsed)
            if program[isp]["op"] == "jmp":
                program[isp]["op"] = "nop"
            elif program[isp]["op"] == "nop":
                program[isp]["op"] = "jmp"
            else:
                isp += 1
                continue
            isp += 1
            loops, acc = does_loop(program)
        return acc


print(part1("input.txt"))
print(part2("input.txt"))