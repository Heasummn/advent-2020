def generate_graph(filename):
    with open(filename) as f:
        graph = {}
        for line in f:
            tokens = line.split()
            current_bag = " ".join(tokens[:3])
            bags_inside = []
            idx = 4
            while idx < len(tokens):
                if tokens[idx] == "no":
                    idx += 3
                elif tokens[idx] == "1":
                    inside = tokens[idx:idx+4]
                    num = int(inside[0])
                    inside[-1] = inside[-1][:-1] + "s" # remove comma or period and add s
                    bags_inside.append((num, " ".join(inside[1:])))
                    idx += 4
                else:
                   inside = tokens[idx:idx+4]
                   num = int(inside[0])
                   inside[-1] = inside[-1][:-1] # remove comma or period
                   bags_inside.append((num, " ".join(inside[1:])))
                   idx += 4
            graph[current_bag] = bags_inside
        return graph

def invert_graph(graph):
    inverted = {}
    for (node, connections) in graph.items():
        for con in connections:
            if con[1] in inverted:
                inverted[con[1]].append(node)
            else:
                inverted[con[1]] = [node]
    return inverted

def part1(filename):
        graph = generate_graph(filename)
        graph = invert_graph(graph)
        to_visit = set(graph['shiny gold bags'])
        visited = set()
        cnt = 0
        while len(to_visit) > 0:
            val = to_visit.pop()
            if val in graph:
                to_visit.update(graph[val])
            if val not in visited:
                cnt += 1
                visited.add(val)
        return cnt

def count_bags(graph, root):
    children = graph[root]
    cnt = 1
    for (number, name) in children:
        print(number, name)
        cnt += number * count_bags(graph, name)
    return cnt

def part2(filename):
   graph = generate_graph(filename)
   return count_bags(graph, 'shiny gold bags') - 1 # the root bag does not contain itself

#print(part1("input.txt"))
print(part2("input.txt"))