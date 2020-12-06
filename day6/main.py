def part1(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
        answers = []
        last_i = 0
        for i, line in enumerate(lines):
            if line == '':
                answers.append(lines[last_i:i])
                last_i = i+1

        # last line gets left out because no newline at the end
        answers.append(lines[last_i:])
        cnt = 0
        for group in answers:
            group_ans = set()
            for person in group:
                group_ans.update(person)
            cnt += len(group_ans)
        return cnt

from collections import Counter

def part2(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
        answers = []
        last_i = 0
        for i, line in enumerate(lines):
            if line == '':
                answers.append(lines[last_i:i])
                last_i = i+1

        # last line gets left out because no newline at the end
        answers.append(lines[last_i:])
        cnt = 0
        for group in answers:
            group_ans = set(group[0])
            for person in group[1:]:
                group_ans = group_ans.intersection(person)
            cnt += len(group_ans)
        return cnt

print(part1("input.txt"))
print(part2("input.txt"))