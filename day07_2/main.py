DATA: list[list[str]] = []

with open('input.txt', 'rt', encoding='utf-8') as f:
    for i in f:
        line: list[str] = []
        for j in i.strip():
            line.append(j)
        DATA.append(line)

def main():
    paths = [ [ 0 for _ in range(len(DATA[i])) ] for i in range(len(DATA)) ]
    paths[0][DATA[0].index('S')] = 1
    for i in range(1, len(DATA)):
        marked: list[int] = []
        for j in range(len(DATA[i])):
            if DATA[i - 1][j] == '|' or DATA[i - 1][j] == 'S':
                if DATA[i][j] == '.':
                    marked.append(j)
                    paths[i][j] += paths[i - 1][j]
                elif DATA[i][j] == '^':
                    marked.append(j - 1)
                    paths[i][j - 1] += paths[i - 1][j]
                    marked.append(j + 1)
                    paths[i][j + 1] += paths[i - 1][j]
        for j in marked:
            DATA[i][j] = '|'
    count = 0
    for i in paths[len(paths) - 1]:
        count += i
    print(count)

main()