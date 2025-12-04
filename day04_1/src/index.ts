import { readFileSync } from "fs";

(() => {
    const input = readFileSync('input.txt', { encoding: 'utf-8' }).trim().split('\n');
    let count = 0;
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
                    count++;
                }
            }
        }
    }
    console.log(count);
})();