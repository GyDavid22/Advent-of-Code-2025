import re

DATA: list[list[str]] = []

with open('input.txt', 'rt', encoding='utf-8') as f:
    text = f.read().strip().split('\n')
    for line in text:
        splitted = re.split(r' +', line)
        sanitized: list[str] = []
        for item in splitted:
            strip = item.strip()
            if not strip == '':
                sanitized.append(strip)
        DATA.append(sanitized)

def main():
    total_sum = 0
    methods = DATA.pop()
    for i in range(len(methods)):
        if methods[i] == '+':
            current_sum = 0
        else:
            current_sum = 1
        for j in range(len(DATA)):
            as_num = int(DATA[j][i])
            if methods[i] == '+':
                current_sum += as_num
            else:
                current_sum *= as_num
        total_sum += current_sum

    print(total_sum)

main()