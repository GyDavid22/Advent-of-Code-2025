DATA: list[tuple[int, int]] = []

with open('input.txt', 'rt', encoding='utf-8') as f:
    for i in f.read().strip().split('\n'):
        (x, y) = [ int(j) for j in i.split(',')]
        DATA.append((x, y))

def main():
    max_size = calc_size(DATA[0], DATA[1])
    for i in range(len(DATA) - 1):
        for j in range(i + 1, len(DATA)):
            size = calc_size(DATA[i], DATA[j])
            if size > max_size:
                max_size = size
    print(max_size)

def calc_size(a: tuple[int, int], b: tuple[int, int]):
    return (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1)

main()