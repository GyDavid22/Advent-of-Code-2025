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
            k = 0
            while k < len(shortest_connections) and shortest_connections[k][2] <= distance:
                k += 1
            shortest_connections.insert(k, (DATA[i], DATA[j], distance))
            if len(shortest_connections) > 1000:
                shortest_connections.pop()
    circuits: list[list[str]] = [ [i] for i in DATA ]
    for i in shortest_connections:
        (a, b) = (i[0], i[1])
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
                    break
    circuits.sort(key=lambda x : len(x), reverse=True)
    multiply = 1
    for i in range(3):
        multiply *= len(circuits[i])
    print(multiply)

main()