DATA: list[str]

with open('input.txt', 'rt', encoding='utf-8') as f:
    file_data = f.read().strip().split('\n')
    for i in range(len(file_data)):
        file_data[i] = file_data[i].strip()
    DATA = file_data

def main():
    i = 0
    ranges: list[tuple[int, int]] = []
    while not DATA[i] == '':
        split = DATA[i].split('-')
        ranges.append((int(split[0]), int(split[1])))
        i += 1
    fresh_count = 0
    for j in range(i + 1, len(DATA)):
        id = int(DATA[j])
        for k in ranges:
            if id >= k[0] and id <= k[1]:
                fresh_count += 1
                break
    print(fresh_count)


main()