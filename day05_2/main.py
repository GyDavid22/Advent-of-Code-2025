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
        (bottom, top) = (int(split[0]), int(split[1]))
        ranges.append((bottom, top))
        i += 1
    ranges.sort(key=lambda r : r[0])
    mergedRanges: list[tuple[int, int]] = []
    currentmin = ranges[0][0]
    currentmax = ranges[0][1]
    for j in range(1, len(ranges)):
        if ranges[j][0] <= currentmax and ranges[j][1] > currentmax:
            currentmax = ranges[j][1]
        elif ranges[j][0] > currentmax:
            mergedRanges.append((currentmin, currentmax))
            currentmin = ranges[j][0]
            currentmax = ranges[j][1]
    mergedRanges.append((currentmin, currentmax))
    fresh_IDs = 0
    for j in mergedRanges:
        fresh_IDs += j[1] - j[0] + 1
    print(fresh_IDs)

main()