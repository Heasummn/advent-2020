import math

def parse_movement(action, degrees):
    direction = action[0]
    val = int(action[1:])
    if direction == 'N':
        return (0, val, 0)
    elif direction == 'S':
        return (0, -val, 0)
    elif direction == 'E':
        return (val, 0, 0)
    elif direction == 'W':
        return -val, 0, 0
    elif direction == 'R':
        return (0, 0, -val)
    elif direction == 'L':
        return (0, 0, val)
    elif direction == 'F':
        x_scale = math.cos(math.radians(degrees))
        y_scale = math.sin(math.radians(degrees))
        return (x_scale * val, y_scale * val, 0)

def part1(filename):
    x = 0
    y = 0
    direction = 0
    with open(filename) as f:
        for line in f:
            dx, dy, dtheta = parse_movement(line, direction)
            x += dx
            y += dy
            direction += dtheta
        return round(abs(x) + abs(y))

def part2(filename):
    waypoint_x = 10
    waypoint_y = 1
    x = 0
    y = 0
    with open(filename) as f:
        for line in f:
            direction = line[0]
            val = int(line[1:])
            if direction == 'N':
                waypoint_y += val
            elif direction == 'S':
                waypoint_y -= val
            elif direction == 'E':
                waypoint_x += val
            elif direction == 'W':
                waypoint_x -= val
            elif direction == 'R':
                s = math.sin(math.radians(-val))
                c = math.cos(math.radians(-val))
                """
                cos -sin  * x
                sin  cos    y
                """
                tmp = waypoint_x
                waypoint_x = c * waypoint_x - s * waypoint_y
                waypoint_y = s * tmp + c * waypoint_y
            elif direction == 'L':
                s = math.sin(math.radians(val))
                c = math.cos(math.radians(val))
                """
                cos -sin  * x
                sin  cos    y
                """
                tmp = waypoint_x
                waypoint_x = c * waypoint_x - s * waypoint_y
                waypoint_y = s * tmp + c * waypoint_y
            elif direction == 'F':
                x += waypoint_x * val
                y += waypoint_y * val
        return round(abs(x) + abs(y))

print(part1("input.txt"))
print(part2("input.txt"))
