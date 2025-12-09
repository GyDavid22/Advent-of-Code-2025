 # needs optimization, ran for ~2 hours

DATA: list[tuple[int, int]] = []

with open('input.txt', 'rt', encoding='utf-8') as f:
    for i in f.read().strip().split('\n'):
        (x, y) = [ int(j) for j in i.split(',')]
        DATA.append((x, y))

def main():
    edge_tiles: list[tuple[int, int]] = []
    for i in range(1, len(DATA)):
        (x1, y1) = (DATA[i - 1][0], DATA[i - 1][1])
        (x2, y2) = (DATA[i][0], DATA[i][1])
        for j in range(min(x1, x2), max(x1, x2) + 1):
            for k in range(min(y1, y2), max(y1, y2) + 1):
                edge_tiles.append((j, k))
    (x1, y1) = (DATA[len(DATA) - 1][0], DATA[len(DATA) - 1][1])
    (x2, y2) = (DATA[0][0], DATA[0][1])
    for j in range(min(x1, x2), max(x1, x2) + 1):
        for k in range(min(y1, y2), max(y1, y2) + 1):
            edge_tiles.append((j, k))
    max_size = None
    for i in range(len(DATA) - 1):
        (x1, y1) = (DATA[i][0], DATA[i][1])
        for j in range(i + 1, len(DATA)):
            (x2, y2) = (DATA[j][0], DATA[j][1])
            found = False
            for k in edge_tiles:
                (x3, y3) = (k[0], k[1])
                if x3 > min(x1, x2) and x3 < max(x1, x2) and y3 > min(y1, y2) and y3 < max(y1, y2):
                    found = True
                    break
            if not found:
                size = calc_size(DATA[i], DATA[j])
                if max_size == None or size > max_size:
                    max_size = size
    print(max_size)

def calc_size(a: tuple[int, int], b: tuple[int, int]):
    return (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1)

main()