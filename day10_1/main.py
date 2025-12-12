from collections import deque

DATA: list[tuple[list[bool], list[list[int]], list[int]]] = []

with open('input.txt', 'rt', encoding='utf-8') as f:
    for i in f.read().strip().split('\n'):
        line = i.strip().split(' ')
        currentLights: list[bool] = [ j == '#' for j in line[0].strip('[').strip(']') ]
        currentButtons: list[list[int]] = []
        for j in range(1, len(line) - 1):
            stripped = line[j].strip('(').strip(')').split(',')
            currentButtons.append([ int(k) for k in stripped ])
        currentJoltages: list[int] = [ int(j) for j in line[len(line) - 1].strip('{').strip('}').split(',') ]
        DATA.append((currentLights, currentButtons, currentJoltages))

def main():
    sum = 0
    for i in DATA:
        q: deque[tuple[list[bool], int, list[int]]] = deque()
        q.append(([ False for _ in range(len(i[0])) ], 0, []))
        solutionFound = False
        foundStates: set[str] = set()
        foundStates.add('.' * len(i[0]))
        while not solutionFound:
            (currentState, currentDepth, lastButtons) = q.popleft()
            for button in i[1]:
                if button == lastButtons:
                    continue
                state = currentState.copy()
                for j in button:
                    state[j] = not state[j]
                depth = currentDepth + 1
                if state == i[0]:
                    sum += depth
                    solutionFound = True
                    break
                else:
                    stateString = ''.join([ '#' if j else '.' for j in state ])
                    if not stateString in foundStates:
                        foundStates.add(stateString)
                        q.append((state, depth, button))
    print(sum)

main()