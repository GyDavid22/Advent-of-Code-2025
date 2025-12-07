DATA: list[list[str]] = []

with open('input.txt', 'rt', encoding='utf-8') as f:
    for i in f:
        line: list[str] = []
        for j in i.strip():
            line.append(j)
        DATA.append(line)

def main():
    splitcount = 0
    for i in range(1, len(DATA)):
        for j in range(len(DATA[i])):
            if DATA[i - 1][j] == '|' or DATA[i - 1][j] == 'S':
                if DATA[i][j] == '.':
                    DATA[i][j] = '|'
                elif DATA[i][j] == '^':
                    splitcount += 1
                    DATA[i][j - 1] = '|'
                    DATA[i][j + 1] = '|'
    print(splitcount)

main()