from collections import Counter

def valid(letter, rng, password):
    count = Counter(password)
    return count[letter] in range(*rng)

def part1(filename):
    cnt = 0
    with open(filename) as f:
        for line in f:
            rng_str, let_str, password = line.split(" ")
            rng_lst = rng_str.split("-")
            rng = int(rng_lst[0]), int(rng_lst[1]) + 1
            letter = let_str[0]
            cnt += int(valid(letter, rng, password))
    return cnt


def part2(filename):
    cnt = 0
    with open(filename) as f:
        for line in f:
            rng_str, let_str, password = line.split(" ")
            rng_lst = rng_str.split("-")
            rng = int(rng_lst[0]) - 1, int(rng_lst[1]) - 1
            letter = let_str[0]
            if (password[rng[0]] == letter or password[rng[1]] == letter) and password[rng[0]] != password[rng[1]]:
                cnt += 1
    return cnt

print(part1("input.txt"))
print(part2("input.txt"))
