import re

DATA: list[list[str]] = []

with open('input.txt', 'rt', encoding='utf-8') as f:
    text = f.read().strip().split('\n')
    last = text.pop()
    currentNums: list[str] = []
    for i in range(len(text[0])):
        current = ''
        allSpaces = True
        for j in range(len(text)):
            char = text[j][i]
            current += char
            if not char == ' ':
                allSpaces = False
        if not allSpaces:
            currentNums.append(current)
        if allSpaces:
            DATA.append(currentNums)
            currentNums = []
    DATA.append(currentNums)
    DATA.append(re.split(r' +', last))

def main():
    total_sum = 0
    methods = DATA.pop()
    for i in range(len(methods)):
        if methods[i] == '+':
            current_sum = 0
        else:
            current_sum = 1
        for j in range(len(DATA[i])):
            as_num = int(DATA[i][j])
            if methods[i] == '+':
                current_sum += as_num
            else:
                current_sum *= as_num
        total_sum += current_sum

    print(total_sum)

main()