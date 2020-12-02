
def part1(filename):
    target = 2020
    nums = set()

    with open(filename) as f:
        for line in f:
            num = int(line)
            nums.add(num)

    for num in nums:
        if target - num in nums:
            return (target - num) * num


def part2(filename):
    target = 2020
    nums = set()
    with open(filename) as f:
        for line in f:
            num = int(line)
            nums.add(num)
    for num1 in nums:
        for num2 in nums:
            if target - num1 - num2 in nums:
                return (target - num1 - num2) * num1 * num2

print(part1("input.txt"))
print(part2("input.txt"))

