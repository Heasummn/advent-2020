def read_file(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
        passports = []
        last_i = 0
        for i, line in enumerate(lines):
            if line == '':
                passports.append(" ".join(lines[last_i:i]))
                last_i = i+1

        # last line gets left out because no newline at the end
        passports.append(" ".join(lines[last_i:]))

        passports = [{key:value for (key, value) in [x.split(':') for x in passport.split(" ")]} for passport in passports]
    return passports

def part1(filename):
        passports = read_file(filename)

        required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
        cnt = 0
        for passport in passports:
            cnt += all(map(lambda x: x in passport.keys(), required_fields))
        return cnt


def convert(passport):
    """
    normalizes passport into correct data types
    """
    passport = passport.copy()
    passport['byr'] = int(passport['byr'])
    passport['iyr'] = int(passport['iyr'])
    passport['eyr'] = int(passport['eyr'])
    passport['hgt'] = (int(''.join(filter(str.isdigit, passport['hgt']))),
        ''.join(filter(str.isalpha, passport['hgt']))
    )

    return passport

valid_hex = list(map(str, range(0, 10))) + ['a', 'b', 'c', 'd', 'e', 'f']
def is_valid(passport):
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    if not all(map(lambda x: x in passport.keys(), required_fields)):
        return False
    passport = convert(passport)
    valid_byr = 1920 <= passport['byr'] <= 2002
    valid_iyr = 2010 <= passport['iyr'] <= 2020
    valid_eyr = 2020 <= passport['eyr'] <= 2030
    hgt, units = passport['hgt']
    valid_hgt = (150 <= hgt <= 193 if units == 'cm' else 59 <= hgt <= 76 if units == 'in' else False)
    valid_hcl = passport['hcl'][0] == '#' and all(map(lambda x: x in valid_hex, passport['hcl'][1:]))
    valid_ecl = passport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    valid_pid = len(passport['pid']) == 9

    return valid_byr and valid_iyr and valid_eyr and valid_hgt and valid_hcl and valid_ecl and valid_pid

def part2(filename):
    passports = read_file(filename)
    cnt = sum(map(is_valid, passports))
    return cnt


print(part1("day4/input.txt"))
print(part2("day4/input.txt"))