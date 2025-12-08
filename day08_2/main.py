import math

DATA: list[str] = []

with open('input.txt', 'rt', encoding='utf-8') as f:
    for i in f.read().strip().split('\n'):
        DATA.append(i.strip())

def main():
    shortest_connections: list[tuple[str, str, float]] = []
    for i in range(len(DATA) - 1):
        for j in range(i + 1, len(DATA)):
            (x_1, y_1, z_1) = [ int(k) for k in DATA[i].split(',') ]
            (x_2, y_2, z_2) = [ int(k) for k in DATA[j].split(',') ]
            distance = math.sqrt(abs((x_1 - x_2) ** 2 + (y_1 - y_2) ** 2 + (z_1 - z_2) ** 2))
            shortest_connections.append((DATA[i], DATA[j], distance))
    shortest_connections.sort(key=lambda x : x[2])
    circuits: list[list[str]] = [ [i] for i in DATA ]
    i = 0
    last_boxes = (shortest_connections[0][0], shortest_connections[0][1])
    while i < len(shortest_connections) and not len(circuits) == 1:
        (a, b) = (shortest_connections[i][0], shortest_connections[i][1])
        a_index = -1
        for j in range(len(circuits)):
            if a in circuits[j]:
                a_index = j
                break
        if not b in circuits[a_index]:
            for j in range(len(circuits)):
                if b in circuits[j]:
                    circuits[a_index].extend(circuits[j])
                    circuits.pop(j)
                    last_boxes = (a, b)
                    break
        i += 1
    print(int(last_boxes[0].split(',')[0]) * int(last_boxes[1].split(',')[0]))

main()