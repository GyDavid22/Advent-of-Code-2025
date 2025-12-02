import { readFileSync } from "fs";

(() => {
    const ranges = readFileSync('input.txt', { encoding: 'utf-8' })
        .trim()
        .split(',')
        .map((val) => val.split('-'));
    let sum = 0;
    const found = new Set();
    for (const element of ranges) {
        const bottom = Number.parseInt(element[0]);
        const top = Number.parseInt(element[1]);
        for (let i = bottom; i <= top; i++) {
            const asString = i.toString();
            const half = Math.floor(asString.length / 2);
            for (let j = 1; j <= half; j++) {
                const regex = new RegExp(`^(${asString.slice(0, j)})+$`);
                if (asString.match(regex) && !found.has(i)) {
                    sum += i;
                    found.add(i);
                }
            }
        }
    }
    console.log(sum);
})();