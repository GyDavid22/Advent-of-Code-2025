import { readFileSync } from "fs";

(() => {
    const input = readFileSync('input.txt', { encoding: 'utf-8' }).trim().split('\n');
    let count = 0;
    let iterationCount = 0;
    do {
        iterationCount = 0;
        const marked: { x: number, y: number; }[] = [];
        for (let i = 0; i < input.length; i++) {
            for (let j = 0; j < input[i].length; j++) {
                if (input[i][j] === '@') {
                    let localCount = 0;
                    for (let k = -1; k <= 1; k++) {
                        for (let l = -1; l <= 1; l++) {
                            const [x, y] = [i + k, j + l];
                            if (x >= 0 && x < input.length && y >= 0 && y < input[i].length && !(k === 0 && l === 0) && input[x][y] === '@') {
                                localCount++;
                            }
                        }
                    }
                    if (localCount < 4) {
                        iterationCount++;
                        marked.push({ x: i, y: j });
                    }
                }
            }
        }
        for (const element of marked) {
            input[element.x] = `${input[element.x].slice(0, element.y)}.${input[element.x].slice(element.y + 1)}`;
        }
        count += iterationCount;
    } while (iterationCount !== 0);
    console.log(count);
})();